import datetime
import itertools
import random

import lorem
import render as r
import render_aggrid as aggrid
import render_html as html
import render_utils
from render_utils.formatters import transform_if_number

TITLE = "AG Grid Example"
FAVICON = "website/static/ag-grid_favicon.png"
NB_ROWS = 100
HEADERS = ["int", "int_blank", "bool", "float", "str", "date", "datetime"]


def app(_window: r.Window):
    def create_line():
        index = 0
        while True:
            index += 1
            even_row = index % 2 == 0
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
    rowData = [dict(zip(HEADERS, row)) for row in values]

    def update_values(index, value):
        values[index][4] = value

    cols = [
        aggrid.AgGridColumn(
            field="int",
            headerName="Integer",
            valueFormatter=transform_if_number(render_utils.numeral),
        ),
        aggrid.AgGridColumn(
            field="str",
            headerName="String",
            cellStyle={"textAlign": "left"},
            editable=True,
            onCellValueChanged=update_values,
            singleClickEdit=True,
        ),
        aggrid.AgGridColumn(
            field="bool",
            headerName="Bool",
            valueFormatter=transform_if_number(render_utils.boolToString),
        ),
        aggrid.AgGridColumn(
            field="float",
            headerName="Float",
            valueFormatter=transform_if_number(render_utils.round_value_to_2_digits),
        ),
        aggrid.AgGridColumn(
            field="date",
            headerName="Date",
            valueFormatter=transform_if_number(render_utils.toLocaleDateString),
        ),
        aggrid.AgGridColumn(
            field="datetime",
            headerName="DateTime",
            valueFormatter=transform_if_number(render_utils.toLocaleDateString),
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
