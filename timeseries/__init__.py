import datetime

import render as r
import render_aggrid as aggrid
import render_antd as antd
import render_html as html

from ..fred import get_fred_series_observations
from .config import COLUMNS


class App:
    def __init__(self, _window):
        controller = r.Controller()
        self.ticker = antd.Input(
            defaultValue="T10Y2Y", style={"width": 120}, controller=controller
        )
        today = datetime.datetime.today()
        start_date = antd.DatePicker(defaultValue=today - datetime.timedelta(days=365))
        end_date = antd.DatePicker(defaultValue=today)
        get_stocks_close = lambda: get_fred_series_observations(
            self.ticker(), start_date(), end_date()
        )
        self.content = html.div(
            aggrid.AgGridReact(
                [
                    aggrid.AgGridColumn(field=name, **col)
                    for name, (_formatter, col) in COLUMNS
                ],
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
        self.title = lambda: self.ticker().upper()
        self.ok = controller.commit
        self.cancel = controller.revert
