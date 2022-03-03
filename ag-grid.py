import random
from datetime import date, datetime

import lorem
from reflect import Callback
from reflect_aggrid import AgGridColumn, AgGridReact
from reflect_html import div
from reflect_utils.formatters import (
    boolToString,
    replace_value,
    round_value_to_2_digits,
    toLocaleDateString,
    toLocaleString,
    numeral,
)

TITLE = "AG Grid Example"
FAVICON = "website/static/ag-grid_favicon.png"
NB_ROWS = 10


editable = {
    "editable": True,
    "enableCellChangeFlash": True,
    "onCellValueChanged": Callback(
        print, args=["data.str", "newValue"]
    ),
    "singleClickEdit": True,
}


def make_editable(definition):
    return dict(definition.items(), **editable)


details = dict(field="int", headerName="Integer", valueValueFormatter=numeral)


def app():
    cols = [
        AgGridColumn(field="str", headerName="String", cellStyle={"textAlign": "left"}),
        AgGridColumn(field="bool", headerName="Bool", valueValueFormatter=boolToString),
        AgGridColumn(**make_editable(details)),
        AgGridColumn(
            field="int_blank",
            headerName="Integer Blank Zeroes",
            valueNumberFormatter=replace_value(toLocaleString, 0, "-"),
        ),
        AgGridColumn(
            field="float",
            headerName="Float",
            valueNumberFormatter=round_value_to_2_digits,
        ),
        AgGridColumn(
            field="date", headerName="Date", valueValueFormatter=toLocaleDateString
        ),
        AgGridColumn(
            field="datetime",
            headerName="DateTime",
            valueValueFormatter=toLocaleDateString,
        ),
    ]
    rowData = {
        "bool": [i % 2 == 0 for i in range(NB_ROWS)],
        "int": [random.randrange(0, 100000) for _ in range(NB_ROWS)],
        "int_blank": [
            random.randrange(0, 100000) if i % 2 == 0 else 0 for i in range(NB_ROWS)
        ],
        "float": [random.uniform(0.0, 100.0) for _ in range(NB_ROWS)],
        "str": [next(lorem.word()) for _ in range(NB_ROWS)],
        "date": [date.today() for _ in range(NB_ROWS)],
        "datetime": [datetime.now() for _ in range(NB_ROWS)],
    }
    grid = AgGridReact(
        cols,
        rowData=rowData,
        rowHeight=24,
        defaultColDef=dict(
            resizable=True, filter=True, cellStyle={"textAlign": "right"}
        ),
        componentDidMount=lambda: grid.autoSizeColumns([col.field for col in cols]),
    )

    return div(
        grid,
        style=dict(width="100%", height=f"{30 + 25 * NB_ROWS}px"),
    )
