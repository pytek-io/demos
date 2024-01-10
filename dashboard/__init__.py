import render as r
import render_antd as antd
import render_antd.utils as antd_utils
import render_html as html
import render_rcdock.utils as rcdock_utils
import render_utils

from demos.charts.altair.car_data_set import App as AltairApp
from demos.stock_prices import App as StockApp
from demos.stocks_history import App as StockHistoryApp
from demos.yahoo_trends import App as YahooTrendApp
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


class App:
    def __init__(self, window: r.Window):
        self.window = window
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
        self.dock_layout = rcdock_utils.DockLayoutRender(
            defaultLayout=defaultLayout, style={"height": "100%", "width": "100%"}
        )

        async def create_stocks_callback(market):
            await self.dock_layout.insert_component(
                StockApp(market), settings_visible=False
            )

        async def create_yahoo_trend_callback():
            await self.dock_layout.insert_component(
                YahooTrendApp(self.window), settings_visible=False
            )

        async def create_live_quotes_callback(tickers):
            await self.dock_layout.insert_component(
                YahooFinanceApp(self.window, tickers)
            )

        menu = antd.Menu(
            items=[
                {
                    "children": [
                        {
                            "type": "group",
                            "children": [
                                {
                                    "label": "Stock history",
                                    "onClick": self.add_StockHistoryApp,
                                },
                                {
                                    "label": "Altair car dataset",
                                    "onClick": lambda: self.dock_layout.insert_component(
                                        AltairApp()
                                    ),
                                },
                            ],
                            "label": "Plotting",
                        },
                        {
                            "type": "group",
                            "children": [
                                {
                                    "label": "NYSE",
                                    "onClick": lambda: create_stocks_callback("nyse"),
                                },
                                {
                                    "label": "AMEX",
                                    "onClick": lambda: create_stocks_callback("amex"),
                                },
                                {
                                    "label": "NASDAQ",
                                    "onClick": lambda: create_stocks_callback("nasdaq"),
                                },
                            ],
                            "label": "Stocks",
                        },
                        {
                            "label": "Yahoo FX live quotes",
                            "onClick": lambda: create_live_quotes_callback(
                                DEFAULT_LIVE_FX_TICKERS
                            ),
                        },
                        {
                            "label": "Yahoo trends",
                            "onClick": create_yahoo_trend_callback,
                        },
                    ],
                    "key": "SubMenu",
                    "icon": render_utils.create_icon(
                        MENU, style={"height": 30, "color": rcdock_utils.LIGHT_GREY}
                    ),
                }
            ],
            selectedKeys=lambda: [],
            mode="horizontal",
            style={"height": "40px"},
        )
        self.content = html.div(
            [
                html.div(menu, style={"flexGrow": 1}),
                html.div(self.dock_layout, style={"height": "100%", "width": "100%"}),
            ],
            style={
                "position": "absolute",
                "height": "100%",
                "width": "100%",
                "display": "flex",
                "flexFlow": "column",
            },
        )

    def create_stock_history_app(self, ticker: str):
        return StockHistoryApp(self.window, r.ObservableValue(ticker), False)

    async def add_StockHistoryApp(self):
        await self.dock_layout.insert_component(
            self.create_stock_history_app("AAPL"), settings_visible=True
        )


app = antd_utils.create_app(App)
