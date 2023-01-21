import base64
import json
import typing

import reflect as r
import reflect_aggrid as aggrid
import reflect_antd as antd
import reflect_html as html
import reflect_utils
import websockets

from .config import COLUMNS, URI
from .yaticker_pb2 import yaticker

TITLE = "YF live quotes"


def load_yahoo_update(message):
    ticker = yaticker()
    ticker.ParseFromString(base64.b64decode(message))
    return ticker


class YFLiveQuoteManager:
    def __init__(self, window: r.Window) -> None:
        self.tickers = set([])
        self.yahoo_connection = None
        self.window = window

    def add_tickers(self, tickers: typing.Iterable[str]):
        if self.yahoo_connection:
            self.yahoo_connection.send_nowait({"subscribe": list(tickers)})
        self.tickers.update(tickers)

    async def remove_ticker(self, ticker):
        self.tickers.remove(ticker)
        self.yahoo_connection.send_nowait({"unsubscribe": [ticker]})

    async def updates(self):
        while True:
            connection_manager = reflect_utils.ws_connection_manager(
                URI,
                self.window.task_group,
                number_messages=False,
                dumps=json.dumps,
                loads=load_yahoo_update,
            )
            async with connection_manager as self.yahoo_connection:
                self.add_tickers(list(self.tickers))
                try:
                    async for message in self.yahoo_connection:
                        if message.id in self.tickers:
                            yield message
                except websockets.exceptions.ConnectionClosedError:
                    print("Yahoo connection has been reset, looping...")


MENU_ITEMS = [{"name": "Remove", "action_tag": "remove quote"}]


class App:
    def __init__(
        self, window: r.Window, initial_tickers: typing.List[str] = []
    ) -> None:
        self.initial_tickers = initial_tickers
        self.window = window
        self.quote_manager = YFLiveQuoteManager(self.window)
        self.content = aggrid.AgGridReact(
            [
                aggrid.AgGridColumn(field=field, **args)
                for field, (_formatter, args) in COLUMNS
            ],
            getRowNodeId=r.js("id"),
            defaultColDef={"resizable": True},
            componentDidMount=self.main,
            getContextMenuItems=r.js("createContextMenu", MENU_ITEMS),
        )
        self.settings = antd.Input(
            placeholder="Enter ticker here", onPressEnter=self.ok, style={"width": 120}
        )
        self.cancel = self.ok
        self.title = "Yahoo live quotes"

    async def ok(self):
        new_ticker = self.settings()
        if new_ticker:
            await self.add_tickers([new_ticker])
            self.settings.set("")

    async def add_tickers(self, tickers):
        await self.content.applyTransactionAsync(
            {"add": [{"id": ticker} for ticker in tickers]}
        )
        self.quote_manager.add_tickers(tickers)

    async def process_messages_from_client(self):
        async for code, data in self.window.client_connection:
            if code == "remove quote":
                ticker = data[0]
                await self.quote_manager.remove_ticker(ticker)
                await self.content.applyTransactionAsync({"remove": [{"id": ticker}]})

    async def main(self):
        self.window.start_soon(self.process_messages_from_client)
        await self.add_tickers(self.initial_tickers)
        async for update in self.quote_manager.updates():
            await self.content.applyTransactionAsync(
                {
                    "update": [
                        {
                            field: decoder(getattr(update, field))
                            for field, (decoder, _) in COLUMNS
                        }
                    ]
                }
            )


def app(window: r.Window):
    hash_argument = window.hash()
    app = App(window, json.loads(hash_argument) if hash_argument else [])
    return html.div([app.settings, app.content], style={"height": "calc(100% - 35px)"})
