from reflect_antd import Menu
from reflect_html import div
from reflect_rcdock import DockLayoutReflect, LIGHT_GREY
from reflect_utils import create_icon
from demos.stocks_history.stocks_history import App as StockHistoryApp
from demos.stock_prices.main import App as StockApp
from demos.yahoofinancelive.main import App as YahooFinanceApp
from demos.charts.altair.car_data_set import App as AltairApp

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
MENU = "M904 160H120c-4.4 0-8 3.6-8 8v64c0 4.4 3.6 8 8 8h784c4.4 0 8-3.6 8-8v-64c0-4.4-3.6-8-8-8zm0 624H120c-4.4 0-8 3.6-8 8v64c0 4.4 3.6 8 8 8h784c4.4 0 8-3.6 8-8v-64c0-4.4-3.6-8-8-8zm0-312H120c-4.4 0-8 3.6-8 8v64c0 4.4 3.6 8 8 8h784c4.4 0 8-3.6 8-8v-64c0-4.4-3.6-8-8-8z"


class Application:
    def __init__(self):
        defaultLayout = {
            "dockbox": {
                "mode": "horizontal",
                "children": [
                    {
                        "mode": "vertical",
                        "children": [
                            {
                                "tabs": [StockHistoryApp(ticker, False)],
                            }
                            for ticker in DEFAULT_TICKERS
                        ]
                        + [
                            {
                                "tabs": [AltairApp()],
                            }
                        ],
                    },
                    {
                        "tabs": [
                            # dict(title="Cars", content=altair_app()),
                            StockApp("nyse"),
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
                StockApp(market), settings_visible=False
            )

        async def create_live_quotes_callback(tickers):
            await self.dock_layout.insert_component(YahooFinanceApp(tickers))

        menu = Menu(
            [
                Menu.SubMenu(
                    [
                        Menu.ItemGroup(
                            [
                                Menu.Item(
                                    "Stock history",
                                    onClick=self.add_StockHistoryApp,
                                ),
                                Menu.Item(
                                    "Altair car dataset",
                                    onClick=lambda: self.dock_layout.insert_component(
                                        AltairApp(),
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
                                DEFAULT_LIVE_FX_TICKERS
                            ),
                        ),
                    ],
                    key="SubMenu",
                    icon=create_icon(
                        MENU,
                        style={"height": 30, "color": LIGHT_GREY},
                    ),
                )
            ],
            selectedKeys=lambda: [],
            mode="horizontal",
            style={"height": "40px"},
        )
        self.root = div(
            [
                div(
                    menu,
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

    async def add_StockHistoryApp(self):
        await self.dock_layout.insert_component(
            StockHistoryApp("AAPL", False),
            settings_visible=True,
        )


def app():
    return Application().root
