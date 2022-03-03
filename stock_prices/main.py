import json
import pathlib

from reflect import (
    Controller,
    get_window,
    memoize,
)
from reflect_aggrid import AgGridColumn, AgGridReact
from reflect_antd import Col, Row, Select
from reflect_antd.button import Button
from reflect_html import div

from .config import COLUMNS



def content(default="nasdaq"):
    controller = Controller()
    ticker = Select(
        [
            Select.Option("Nasdaq", value="nasdaq"),
            Select.Option("Amex", value="amex"),
            Select.Option("NYSE", value="nyse"),
        ],
        defaultValue=default,
        style=dict(width=120),
        controller=controller,
    )

    # this method will be memoized and its update will be controlled by controller
    @memoize(controller=controller)
    def get_stocks_close():
        # Downloaded from "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&exchange=nyse"
        # It would be more realistic to fetch those directly but NSADQ disabled programmatic access...
        file_path = (
            pathlib.Path(__file__)
            .parent.joinpath("nasdaq")
            .joinpath(f"{ticker()}.json")
            .resolve()
        )
        return json.loads(open(file_path, "r").read())["data"]

    def rowData():
        return [
            {name: formatter(record[name]) for name, (formatter, _col) in COLUMNS}
            for record in get_stocks_close()["table"]["rows"]
        ]

    grid = AgGridReact(
        [AgGridColumn(field=name, **col) for name, (_formatter, col) in COLUMNS],
        rowData=rowData,
        rowHeight=24,
        className="ag-theme-balham",
        defaultColDef=dict(resizable=True, filter=True, cellStyle={"textAlign": "right"}),
    )

    return {
        "title": lambda: ticker().upper(),
        "settings": ticker,
        "ok": controller.commit,
        "cancel": controller.revert,
        "content": grid,
    }


def app():
    app = content()
    get_window().set_title(app["title"])
    return div(
        [
            Row(
                [
                    Col(app["settings"]),
                    Col(
                        Button(
                            ["Update"],
                            type="primary",
                            onClick=app["ok"],
                        )
                    ),
                ],
                gutter=20,
                style=dict(margin=10),
            ),
            div(
                app["content"],
                style=dict(height="calc(100% - 50px)"),
            ),
        ],
        style=dict(
            height="100%",
        ),
    )
