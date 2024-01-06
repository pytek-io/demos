from render_html import *
from render_antd import Table
def app():
    return Table(""{record.description}"", columns=columns, expandable="{!       expandedRowRender: record => <p style=", {!=True, margin:=True, 0=True, !}"=True)