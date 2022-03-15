import json
import pathlib

from reflect import Controller, memoize
from reflect_aggrid import AgGridColumn, AgGridReact
from reflect_antd import Select
from reflect_html import div
from .config import COLUMNS


class App:
    def __init__(self, default="nasdaq"):
        controller = Controller()
        self.settings = Select(
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
                .joinpath(f"{self.settings()}.json")
                .resolve()
            )
            return json.loads(open(file_path, "r").read())["data"]

        def rowData():
            return [
                {name: formatter(record[name]) for name, (formatter, _col) in COLUMNS}
                for record in get_stocks_close()["table"]["rows"]
            ]

        self.content = div(
            AgGridReact(
                [
                    AgGridColumn(field=name, **col)
                    for name, (_formatter, col) in COLUMNS
                ],
                rowData=rowData,
                rowHeight=24,
                className="ag-theme-balham",
                defaultColDef=dict(
                    resizable=True, filter=True, cellStyle={"textAlign": "right"}
                ),
            ),
            style={"height": "100%", "width": "100%"},
        )
        self.title = lambda: self.settings().upper()
        self.ok = controller.commit
        self.cancel = controller.revert
