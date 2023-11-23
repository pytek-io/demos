import pathlib
import json

import pandas as pd
import reflect as r
import reflect_aggrid as aggrid
import reflect_antd as antd
import reflect_html as html

from .config import COLUMNS


class App:
    def __init__(self, window: r.Window, default="nasdaq"):
        controller = r.Controller()
        self.settings = antd.Select(
            options=[
                {"children": "Nasdaq", "value": "nasdaq"},
                {"children": "Amex", "value": "amex"},
                {"children": "NYSE", "value": "nyse"},
            ],
            defaultValue=default,
            style={"width": 120},
            controller=controller,
        )

        def get_stocks_close():
            path = pathlib.Path(__file__).parent.joinpath(
                "nasdaq", f"{self.settings()}.json"
            )
            data = json.loads((path.read_text()))["data"]["table"]
            return pd.DataFrame(data["rows"], columns=data["headers"])

        self.content = html.div(
            aggrid.AgGridReact(
                [aggrid.AgGridColumn(field=name, **col) for name, col in COLUMNS],
                rowData=get_stocks_close,
                rowHeight=24,
                className="ag-theme-balham",
                defaultColDef={
                    "resizable": True,
                    "filter": True,
                    "cellStyle": {"textAlign": "right"},
                },
            ),
            style={"height": "100%", "width": "100%"},
        )
        self.title = lambda: self.settings().upper()
        self.ok = controller.commit
        self.cancel = controller.revert
