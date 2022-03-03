from reflect import get_window
from reflect_antd import Menu, Col, Row
from reflect_html import div, img
from reflect_rcdock import DockLayoutReflect

from demos.stocks_history.stocks_history import (
    DEFAULT_TICKER,
    content as stock_history_content,
)
from demos.stock_prices.main import content as stock_content
from demos.yahoofinancelive.main import content as yf_demo
from demos.altair.car_data_set import content as altair_content

TITLE = "Dashboard"
DEFAULT_TICKERS = ["AMZN"]
DEFAULT_LIVE_INDEX_TICKERS = [
    "^GSPC",
    "^FCHI",
    "^FTSE",
    "^FTMC",
    "^N225",
    "^HSI",
    "^DJI",
]
DEFAULT_LIVE_FX_TICKERS = [
    "BTC-USD",
    "EURUSD=X",
    "GBPEUR=X",
    "EURCAD=X",
    "EURNOK=X",
    "EURSEK=X",
    "EURJPY=X",
]


class App:
    def __init__(self):
        window = get_window()
        defaultLayout = {
            "dockbox": {
                "mode": "horizontal",
                "children": [
                    {
                        "mode": "vertical",
                        "children": [
                            {
                                "tabs": [stock_history_content(ticker, False)],
                            }
                            for ticker in DEFAULT_TICKERS
                        ]
                        + [
                            {
                                "tabs": [altair_content()],
                            }
                        ],
                    },
                    {
                        "tabs": [
                            # dict(title="Cars", content=altair_app()),
                            stock_content("nyse"),
                        ],
                    },
                ],
            }
        }
        self.dock_layout = DockLayoutReflect(
            defaultLayout=defaultLayout,
            style={
                "height": "100%",
                "width": "100%",
            },
        )

        async def create_stocks_callback(market):
            await self.dock_layout.insert_component(
                settings_visible=False, **stock_content(market)
            )

        async def create_live_quotes_callback(tickers, title):
            demo = yf_demo(window, tickers)
            await self.dock_layout.insert_component(
                title=title,
                content=demo["content"],
                settings=demo["settings"],
                ok=demo["ok"],
            )

        menu = Menu(
            [
                Menu.SubMenu(
                    [
                        Menu.ItemGroup(
                            [
                                Menu.Item(
                                    "Stock history",
                                    onClick=self.add_stock_history_content,
                                ),
                                Menu.Item(
                                    "Altair car dataset",
                                    onClick=lambda: self.dock_layout.insert_component(
                                        **altair_content(),
                                    ),
                                ),
                            ],
                            title="Plotting",
                        ),
                        Menu.ItemGroup(
                            [
                                Menu.Item(
                                    "NYSE",
                                    onClick=lambda: create_stocks_callback("nyse"),
                                ),
                                Menu.Item(
                                    "AMEX",
                                    onClick=lambda: create_stocks_callback("amex"),
                                ),
                                Menu.Item(
                                    "NASDAQ",
                                    onClick=lambda: create_stocks_callback("nasdaq"),
                                ),
                            ],
                            title="Stocks",
                        ),
                        Menu.Item(
                            "FX live quotes",
                            onClick=lambda: create_live_quotes_callback(
                                DEFAULT_LIVE_FX_TICKERS, "Live quotes"
                            ),
                        ),
                    ],
                    key="SubMenu",
                    icon=img(
                        alt="pytek menu",
                        src="website/static/menu-icon_grey.svg",
                        style={
                            "height": 30,
                        },
                    ),
                )
            ],
            selectedKeys=lambda: [],
            mode="horizontal",
        )
        self.root = div(
            [
                div(
                    Row(Col(menu), justify="end", align="middle"),
                    style={"flexGrow": 1},
                ),
                div(
                    self.dock_layout,
                    style={
                        "height": "100%",
                        "width": "100%",
                    },
                ),
            ],
            style=dict(
                position="absolute",
                height="100%",
                width="100%",
                display="flex",
                flexFlow="column",
            ),
        )

    async def add_stock_history_content(self):
        await self.dock_layout.insert_component(
            settings_visible=True, **stock_history_content("AAPL", False)
        )


def app():
    return App().root
