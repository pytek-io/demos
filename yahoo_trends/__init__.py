import json

import httpx
import pandas as pd
import render as r
import render_aggrid as aggrid
import render_antd as antd
import render_html as html

from .screeners import SCREENERS
from .cols import FIELDS

URL = "https://query2.finance.yahoo.com/v1/finance/screener/predefined/saved"
PARAMS = {
    "formatted": "false",
    "lang": "en-US",
    "region": "US",
    "corsDomain": "finance.yahoo.com",
}


def get_screener(name: str):
    return pd.DataFrame(
        json.loads(
            httpx.get(
                URL, params={"count": 50, "scrIds": SCREENERS[name]["id"], **PARAMS}
            ).content
        )["finance"]["result"][0]["quotes"]
    )


class App:
    def __init__(self, _: r.Window):
        controller = r.Controller()
        self.settings = antd.Select(
            options=[
                {
                    "label": record["title"],
                    "value": name,
                }
                for name, record in SCREENERS.items()
            ],
            defaultValue=next(iter(SCREENERS)),
            style={"width": 220},
            controller=controller,
        )
        cols = [aggrid.AgGridColumn(field=name) for name in FIELDS]
        grid = aggrid.AgGridReact(
            cols,
            rowData=lambda: get_screener(self.settings()),
            rowHeight=24,
            className="ag-theme-balham",
            defaultColDef={
                "resizable": True,
                "filter": True,
                "cellStyle": {"textAlign": "right"},
            },
            onGridReady=lambda: grid.autoSizeColumns([col.field for col in cols]),
        )
        self.content = html.div(grid, style={"height": "100%", "width": "100%"})
        self.title = lambda: SCREENERS[self.settings()]["title"]
        self.ok = controller.commit
        self.cancel = controller.revert
