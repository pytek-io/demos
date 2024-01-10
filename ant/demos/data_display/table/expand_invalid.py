from render_antd import Table
from render_html import *


def app(_):
    return Table(""{record.description}"", columns=columns, expandable="{!       expandedRowRender: record => <p style=", {!=True, margin:=True, 0=True, !}"=True)