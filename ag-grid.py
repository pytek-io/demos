from itertools import count, islice
import random
from datetime import date, datetime

import lorem
from reflect import Callback
from reflect_aggrid import AgGridColumn, AgGridReact
from reflect_html import div
from reflect_utils.formatters import (
    boolToString,
    round_value_to_2_digits,
    toLocaleDateString,
    numeral,
)

TITLE = "AG Grid Example"
FAVICON = "website/static/ag-grid_favicon.png"
NB_ROWS = 100


def app():
    def create_line():
        index = count(0)
        while True:
            index_value = next(index)
            even_row = index_value == 0
            yield [
                random.randrange(0, 100000),
                random.randrange(0, 100000) if even_row else 0,
                even_row,
                random.uniform(0.0, 100.0),
                next(lorem.word()),
                date.today(),
                datetime.now(),
            ]

    values = list(islice(create_line(), 0, NB_ROWS))
    rowData = dict(
        zip(
            [
                "id",
                "int",
                "int_blank",
                "bool",
                "float",
                "str",
                "date",
                "datetime",
            ],
            [list(range(NB_ROWS))] + list(zip(*values)),
        ),
    )
    editable = {
        "editable": True,
        "enableCellChangeFlash": True,
        "onCellValueChanged": Callback(print, args=["data.int", "newValue"]),
        "singleClickEdit": True,
    }
    def update_values(update):
        index, value = update
        values[index][4] = value

    cols = [
        AgGridColumn(field="id", headerName="id", hide=True),
        AgGridColumn(field="int", headerName="Integer", valueValueFormatter=numeral),
        AgGridColumn(
            field="str",
            headerName="String",
            cellStyle={"textAlign": "left"},
            editable=True,
            onCellValueChanged=Callback(
                update_values, args=["data.id", "newValue"]
            ),
            singleClickEdit=True,
        ),
        AgGridColumn(field="bool", headerName="Bool", valueValueFormatter=boolToString),
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
        style=dict(width="100%", height="50vh"),
    )
