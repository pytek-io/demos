import reflect_aggrid as aggrid
import reflect_antd as antd
import reflect_html as html
import datetime
import reflect as r

from .config import COLUMNS
from ..fred import get_fred_series_observations


class App:
    def __init__(self, default="T10Y2Y"):
        controller = r.Controller()
        self.ticker = antd.Input(
            defaultValue=default,
            style=dict(width=120),
            controller=controller,
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
                defaultColDef=dict(
                    resizable=True, filter=True, cellStyle={"textAlign": "right"}
                ),
            ),
            style={"height": "100%", "width": "100%"},
        )
        self.title = lambda: self.ticker().upper()
        self.ok = controller.commit
        self.cancel = controller.revert
