import pathlib
from itertools import chain

import altair as alt
import pandas as pd
from reflect import get_window, js
from reflect_aggrid import AgGridReact, create_ag_grid_column
from reflect_altair import Chart
from reflect_antd import Menu, Row, Col
from reflect_html import div, img
from reflect_rcdock import DockLayoutReflect
from reflect_utils.md_parsing import parse_md_doc

from .charts import create_performance_chart
from .config import INSTRUMENT_HISTORY, INSTRUMENTS
from .server import Server

PL_CHART = "pnl_chart"
DISPLAY_INSTRUMENT_HISTORY = "instrument_data"

SESSION_MENU_ITEMS = [
    dict(name="History chart", action_tag=PL_CHART),
    dict(name="Display history", action_tag=DISPLAY_INSTRUMENT_HISTORY),
]
URI = "wss://test.deribit.com/ws/api/v2"
GREEN = "#57A44C"
BLUE = "#5276A7"
RED = "#FF0000"
TITLE = "Option backtester"


def dataframe_to_ag_grid(df, id_name):
    columns_as_list = list(df.columns)
    relevant_fields = [
        (columns_as_list.index(column.field), column.field, column.preprocess)
        for column in chain(
            INSTRUMENTS, chain.from_iterable(col.children for col in INSTRUMENTS)
        )
        if column.field
    ]
    id_name = None
    rowData = [
        {
            field: preprocess(record[index]) if preprocess else record[index]
            for index, field, preprocess in relevant_fields
        }
        for record in map(tuple, df.to_records(index=False))
    ]
    return AgGridReact(
        [create_ag_grid_column(column) for column in INSTRUMENTS],
        rowData=rowData,
        rowHeight=24,
        defaultColDef=dict(resizable=True, filter=True, sortable=True),
        getContextMenuItems=js("createContextMenu", SESSION_MENU_ITEMS),
        getRowNodeId=js("fetch_attribute", id_name),
    )


def get_currency_historical_data(currency):
    result = pd.read_csv(
        f"demos/crypto_backtester/HistoricalData_{currency}.csv", index_col=False
    )
    return result.rename(columns={"Close/Last": "Close", "Date": "ticks"})


class App(Server):
    def __init__(self, window, debug=False):
        super().__init__(window, debug)
        welcome_panel = parse_md_doc(
            open(
                pathlib.Path(__file__).parent.joinpath("welcome.md").resolve(), "r"
            ).read()
        )
        defaultLayout = {
            "dockbox": {
                "mode": "vertical",
                "children": [
                    {
                        "tabs": [
                            dict(
                                content=welcome_panel,
                                title="Get started",
                                closeable=False,  # rmk this is not closeable as dock manager enters an invalid state (from our end at least) when it is empty
                            )
                        ],
                    },
                ],
            }
        }
        self.dock_layout = DockLayoutReflect(
            defaultLayout=defaultLayout,
            style={
                "position": "absolute",
                "left": 0,
                "top": 50,
                "right": 0,
                "bottom": 0,
            },
        )

        menu = Menu(
            [
                Menu.SubMenu(
                    [
                        Menu.ItemGroup(
                            [
                                Menu.Item(
                                    "BTC",
                                    onClick=lambda: self.display_instrument_list("BTC"),
                                ),
                                Menu.Item(
                                    "ETH",
                                    onClick=lambda: self.display_instrument_list("ETH"),
                                ),
                            ],
                            title="Instruments",
                        ),
                        Menu.ItemGroup(
                            [
                                Menu.Item(
                                    "BTC",
                                    onClick=lambda: self.display_currency_chart("BTC"),
                                ),
                                Menu.Item(
                                    "ETH",
                                    onClick=lambda: self.display_currency_chart("ETH"),
                                ),
                            ],
                            title="Currencies",
                        ),
                    ],
                    icon=img(
                        alt="menu",
                        src="website/static/menu-icon_grey.svg",
                        style={
                            "height": 30,
                        },
                    ),
                ),
            ],
            mode="horizontal",
            selectedKeys=lambda: [],
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
        # self.root = div([menu, self.dock_layout])

    async def display_instrument_list(self, currency: str):
        async def populate_instruments():
            instruments = await self.get_instruments_for_currency(currency)
            if self.DEBUG:
                import pickle

                open(f"{currency}_instruments.pick", "wb").write(
                    pickle.dumps(instruments)
                )
            await grid.applyTransactionAsync({"add": instruments})

        grid = AgGridReact(
            [create_ag_grid_column(column) for column in INSTRUMENTS],
            rowData=[],
            rowHeight=24,
            className="ag-theme-balham",
            defaultColDef=dict(resizable=True, filter=True, sortable=True),
            getContextMenuItems=js("createContextMenu", SESSION_MENU_ITEMS),
            getRowNodeId=js("fetch_attribute", "instrument_name"),
            componentDidMount=populate_instruments,
        )
        await self.dock_layout.insert_component(f"{currency} options", grid)

    async def display_currency_chart(self, currency):
        source = get_currency_historical_data(currency)
        if self.DEBUG:
            import pickle

            open(f"{currency}.pick", "wb").write(pickle.dumps(source))
        base = alt.Chart(source).encode(
            alt.X(
                "ticks:T",
                axis=alt.Axis(
                    format="%m/%y" if source.shape[0] > 180 else "%d/%m",
                    labelAngle=-45,
                    title=None,
                ),
            ),
            color=alt.condition(
                "datum.Open <= datum.Close", alt.value("#06982d"), alt.value("#ae1325")
            ),
        )
        rule = base.mark_rule().encode(
            alt.Y(
                "Low:Q",
                title="Price",
                scale=alt.Scale(zero=False),
            ),
            alt.Y2("High:Q"),
        )
        bar = base.mark_bar().encode(alt.Y("Open:Q"), alt.Y2("Close:Q"))
        await self.dock_layout.insert_component(
            currency,
            Chart(
                (rule + bar)
                .interactive()
                .properties(width="container", height="container"),
                style={
                    "height": "100%",
                    "width": "100%",
                },
            ),
        )

    async def process_client_messages(self):
        await self.connection_ready.wait()
        async for code, args in self.window.client_connection:
            if code == PL_CHART:
                for instrument_name in args:
                    await self.display_instrument_chart(instrument_name)
            elif code == DISPLAY_INSTRUMENT_HISTORY:
                for instrument_name in args:
                    await self.display_instrument_history(instrument_name)

    async def display_instrument_chart(self, instrument_name):
        df, strike = await self.create_perf_chart_data(instrument_name)
        await self.dock_layout.insert_component(
            instrument_name,
            Chart(
                create_performance_chart(df, strike),
                style={"height": "42.5%", "width": "90%"},
            ),
        )

    async def display_instrument_history(self, instrument_name):
        await self.dock_layout.insert_component(
            instrument_name,
            AgGridReact(
                [create_ag_grid_column(column) for column in INSTRUMENT_HISTORY],
                rowData=await self.get_instrument_data(instrument_name),
            ),
            className="ag-theme-balham",
        )


async def app():
    window = get_window()
    app = App(window, debug=True)
    window.start_soon(app.process_client_messages)

    async def load_a_few_tabs():
        await app.connection_ready.wait()
        await app.display_instrument_list("BTC")
        await app.display_instrument_chart("BTC-24JUN22-30000-C")

    window.start_soon(load_a_few_tabs)
    return app.root
