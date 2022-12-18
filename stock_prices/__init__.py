import json
import pathlib

import reflect_aggrid as aggrid
import reflect_antd as antd
import reflect_html as html

import reflect as r

from .config import COLUMNS


class App:
    def __init__(self, default="nasdaq"):
        controller = r.Controller()
        self.settings = antd.Select(
            options=[
                {"children": "Nasdaq", "value": "nasdaq"},
                {"children": "Amex", "value": "amex"},
                {"children": "NYSE", "value": "nyse"},
            ],
            defaultValue=default,
            style=dict(width=120),
            controller=controller,
        )

        def get_stocks_close():
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

        self.content = html.div(
            aggrid.AgGridReact(
                [
                    aggrid.AgGridColumn(field=name, **col)
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
