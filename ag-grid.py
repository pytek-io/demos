import datetime
import itertools
import random

import lorem
import reflect as r
import reflect_aggrid as aggrid
import reflect_html as html
import reflect_utils

TITLE = "AG Grid Example"
FAVICON = "website/static/ag-grid_favicon.png"
NB_ROWS = 100


def app():
    def create_line():
        index = itertools.count(0)
        while True:
            index_value = next(index)
            even_row = index_value == 0
            yield [
                random.randrange(0, 100000),
                random.randrange(0, 100000) if even_row else 0,
                even_row,
                random.uniform(0.0, 100.0),
                next(lorem.word()),
                datetime.date.today(),
                datetime.datetime.now(),
            ]

    values = list(itertools.islice(create_line(), 0, NB_ROWS))
    rowData = dict(
        zip(
            ["id", "int", "int_blank", "bool", "float", "str", "date", "datetime"],
            [list(range(NB_ROWS))] + list(zip(*values)),
        )
    )

    def update_values(update):
        index, value = update
        values[index][4] = value

    cols = [
        aggrid.AgGridColumn(field="id", headerName="id", hide=True),
        aggrid.AgGridColumn(
            field="int", headerName="Integer", valueValueFormatter=reflect_utils.numeral
        ),
        aggrid.AgGridColumn(
            field="str",
            headerName="String",
            cellStyle={"textAlign": "left"},
            editable=True,
            onCellValueChanged=r.Callback(update_values, [[0, "data", "id"], [0, "newValue"]]),
            singleClickEdit=True,
        ),
        aggrid.AgGridColumn(
            field="bool",
            headerName="Bool",
            valueValueFormatter=reflect_utils.boolToString,
        ),
        aggrid.AgGridColumn(
            field="float",
            headerName="Float",
            valueNumberFormatter=reflect_utils.round_value_to_2_digits,
        ),
        aggrid.AgGridColumn(
            field="date",
            headerName="Date",
            valueValueFormatter=reflect_utils.toLocaleDateString,
        ),
        aggrid.AgGridColumn(
            field="datetime",
            headerName="DateTime",
            valueValueFormatter=reflect_utils.toLocaleDateString,
        ),
    ]
    grid = aggrid.AgGridReact(
        cols,
        rowData=rowData,
        rowHeight=24,
        defaultColDef={
            "resizable": True,
            "filter": True,
            "cellStyle": {"textAlign": "right"},
        },
        onGridReady=lambda: grid.autoSizeColumns([col.field for col in cols]),
    )
    return html.div(grid, style={"width": "100%", "height": "50vh"})
