import reflect as r
import reflect_antd as antd
import reflect_html as html
import reflect_rcdock as rcdock
import reflect_utils

from demos.charts.altair.car_data_set import App as AltairApp
from demos.stock_prices import App as StockApp
from demos.stocks_history import App as StockHistoryApp
from demos.yahoofinancelive import App as YahooFinanceApp

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
                            {"tabs": [self.create_stock_history_app(ticker)]}
                            for ticker in DEFAULT_TICKERS
                        ]
                        + [{"tabs": [AltairApp()]}],
                    },
                    {"tabs": [StockApp("nyse")]},
                ],
            }
        }
        self.dock_layout = rcdock.DockLayoutReflect(
            defaultLayout=defaultLayout, style={"height": "100%", "width": "100%"}
        )

        async def create_stocks_callback(market):
            await self.dock_layout.insert_component(
                StockApp(market), settings_visible=False
            )

        async def create_live_quotes_callback(tickers):
            await self.dock_layout.insert_component(YahooFinanceApp(tickers))

        menu = antd.Menu(
            [
                antd.Menu.SubMenu(
                    [
                        antd.Menu.ItemGroup(
                            [
                                antd.Menu.Item(
                                    "Stock history", onClick=self.add_StockHistoryApp
                                ),
                                antd.Menu.Item(
                                    "Altair car dataset",
                                    onClick=lambda: self.dock_layout.insert_component(
                                        AltairApp()
                                    ),
                                ),
                            ],
                            title="Plotting",
                        ),
                        antd.Menu.ItemGroup(
                            [
                                antd.Menu.Item(
                                    "NYSE",
                                    onClick=lambda: create_stocks_callback("nyse"),
                                ),
                                antd.Menu.Item(
                                    "AMEX",
                                    onClick=lambda: create_stocks_callback("amex"),
                                ),
                                antd.Menu.Item(
                                    "NASDAQ",
                                    onClick=lambda: create_stocks_callback("nasdaq"),
                                ),
                            ],
                            title="Stocks",
                        ),
                        antd.Menu.Item(
                            "FX live quotes",
                            onClick=lambda: create_live_quotes_callback(
                                DEFAULT_LIVE_FX_TICKERS
                            ),
                        ),
                    ],
                    key="SubMenu",
                    icon=reflect_utils.create_icon(
                        MENU, style={"height": 30, "color": rcdock.LIGHT_GREY}
                    ),
                )
            ],
            selectedKeys=lambda: [],
            mode="horizontal",
            style={"height": "40px"},
        )
        self.root = html.div(
            [
                html.div(menu, style={"flexGrow": 1}),
                html.div(self.dock_layout, style={"height": "100%", "width": "100%"}),
            ],
            style=dict(
                position="absolute",
                height="100%",
                width="100%",
                display="flex",
                flexFlow="column",
            ),
        )

    def create_stock_history_app(self, ticker: str):
        return StockHistoryApp(r.ObservableValue(ticker), False)

    async def add_StockHistoryApp(self):
        await self.dock_layout.insert_component(
            self.create_stock_history_app("AAPL"), settings_visible=True
        )


def app():
    return Application().root
