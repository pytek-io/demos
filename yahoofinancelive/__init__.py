import base64
from json import dumps, loads
from typing import Iterable, List

import websockets
from reflect import Window, get_window, js
from reflect_aggrid import AgGridColumn, AgGridReact
from reflect_antd import Input
from reflect_html import div
from reflect_utils import ws_connection_manager

from .config import COLUMNS, URI
from .yaticker_pb2 import yaticker

TITLE = "YF live quotes"


def load_yahoo_update(message):
    ticker = yaticker()
    ticker.ParseFromString(base64.b64decode(message))
    return ticker


class YFLiveQuoteManager:
    def __init__(self, window: Window) -> None:
        self.tickers = set([])
        self.yahoo_connection = None
        self.window = window

    def add_tickers(self, tickers: Iterable[str]):
        if self.yahoo_connection:
            self.yahoo_connection.send_nowait({"subscribe": list(tickers)})
        self.tickers.update(tickers)

    async def remove_ticker(self, ticker):
        self.tickers.remove(ticker)
        self.yahoo_connection.send_nowait({"unsubscribe": [ticker]})

    async def updates(self):
        while True:
            connection_manager = ws_connection_manager(
                URI,
                self.window.task_group,
                number_messages=False,
                dumps=dumps,
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


MENU_ITEMS = [
    dict(
        name="Remove",
        action_tag="remove quote",
    ),
]


class App:
    def __init__(
        self,
        initial_tickers: List[str] = [],
    ) -> None:
        self.initial_tickers = initial_tickers
        self.window = get_window()
        self.quote_manager = YFLiveQuoteManager(self.window)
        self.content = AgGridReact(
            [
                AgGridColumn(field=field, **args)
                for field, (_formatter, args) in COLUMNS
            ],
            getRowNodeId=js("id"),
            defaultColDef=dict(resizable=True),
            componentDidMount=self.main,
            getContextMenuItems=js("createContextMenu", MENU_ITEMS),
        )
        self.settings = Input(
            placeholder="Enter ticker here",
            onPressEnter=self.ok,
            style=dict(width=120),
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


def app():
    hash_argument = get_window().hash()
    app = App(loads(hash_argument) if hash_argument else [])
    return div(
        [app.settings, app.content],
        style=dict(height="calc(100% - 35px)"),  #  -> full screen
    )
