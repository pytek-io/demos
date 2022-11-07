import datetime
import itertools
import json
import pickle
import time

import anyio
import reflect as r
import reflect_utils
import websockets

from .analytics import compute_implied_vols, merge_data
from .utils import to_timestamp

URI = "wss://test.deribit.com/ws/api/v2"
CURRENCIES = [("Bit Coin", "BTC"), ("Etherum", "ETH")]


class PendingResult:
    def __init__(self) -> None:
        self.ready = anyio.Event()
        self.result = None
        self.is_error = True

    async def wait(self):
        await self.ready.wait()
        if self.is_error:
            raise Exception(self.result)
        return self.result

    def set(self, result, is_error):
        self.is_error = is_error
        self.result = result
        self.ready.set()


class Server:
    def __init__(self, window: r.Window, debug=False):
        self.window: r.Window = r.get_window()
        self.request_id = itertools.count()
        self.pending_queries = {}
        self.connection_ready = anyio.Event()
        self.default_start_date = datetime.datetime(2015, 1, 1)
        self.default_end_date = datetime.datetime.today()
        self.default_resolution = "1D"
        self.DEBUG = debug
        self.window.start_soon(self.main)

    async def main(self):
        last_connection_attempt = time.perf_counter()
        while True:
            try:
                connection_manager = reflect_utils.ws_connection_manager(
                    uri=URI,
                    task_group=self.window.task_group,
                    dumps=json.dumps,
                    loads=json.loads,
                    number_messages=False,
                )
                async with connection_manager as self.derebit_connection:
                    self.connection_ready.set()
                    async for response in self.derebit_connection:
                        if "id" in response:
                            is_error = "error" in response
                            self.pending_queries.pop(response["id"]).set(
                                response["error" if is_error else "result"], is_error
                            )
                        else:
                            print(response)
            except websockets.ConnectionClosed as e:
                if time.perf_counter() - last_connection_attempt < 1.0:
                    raise Exception("Connection with Derebit lost.") from e
                print(f"Derebit connection has been closed: {e}, looping...")
                last_connection_attempt = time.perf_counter()

    async def query_derebit(self, method, params={}):
        await self.connection_ready.wait()
        request_id = next(self.request_id)
        await self.derebit_connection.send(
            dict(jsonrpc="2.0", id=request_id, method="public/" + method, params=params)
        )
        pending_result = self.pending_queries[request_id] = PendingResult()
        try:
            return await pending_result.wait()
        except Exception as e:
            raise Exception(f"An error has occurred while querying derebit {e}")

    async def get_currency_data(self, currency, start, end, resolution):
        return await self.query_derebit(
            "get_tradingview_chart_data",
            {
                "instrument_name": currency + "-PERPETUAL",
                "start_timestamp": to_timestamp(start),
                "end_timestamp": to_timestamp(end),
                "resolution": resolution,
            },
        )

    async def get_instrument_data(
        self, instrument_name, start=None, end=None, resolution=None
    ):
        return await self.query_derebit(
            "get_tradingview_chart_data",
            {
                "instrument_name": instrument_name,
                "start_timestamp": to_timestamp(start or self.default_start_date),
                "end_timestamp": to_timestamp(end or self.default_end_date),
                "resolution": resolution or self.default_resolution,
            },
        )

    async def get_instruments_for_currency(self, currency: str):
        return await self.query_derebit(
            "get_instruments",
            {"currency": currency, "kind": "option", "expired": False},
        )

    async def get_instruments(self):
        instruments = []
        for _name, acronym in CURRENCIES:
            instruments.extend(await self.get_instruments_for_currency(acronym))
        return instruments

    async def create_perf_chart_data(self, instrument_name):
        _, expiry, strike, option_type = instrument_name.split("-")
        expiry, strike, option_type = (
            datetime.datetime.strptime(expiry, "%d%b%y"),
            int(strike),
            option_type.lower(),
        )
        instrument_data = await self.get_instrument_data(
            instrument_name,
            self.default_start_date,
            self.default_end_date,
            self.default_resolution,
        )
        currency_data = await self.get_currency_data(
            instrument_name[:3],
            self.default_start_date,
            self.default_end_date,
            self.default_resolution,
        )
        df = merge_data(instrument_data, currency_data)
        df["ivol_mid"] = (
            compute_implied_vols(df, strike, expiry, r=0.01, option_type=option_type)
            * 100
        )
        if self.DEBUG:
            import pandas as pd

            df = pd.DataFrame({name: df[name] for name in df.columns})
            open(f"{instrument_name}.pick", "wb").write(pickle.dumps(df))
        return df, strike
