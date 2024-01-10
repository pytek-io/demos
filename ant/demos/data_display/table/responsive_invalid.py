from render_antd import Table
from render_html import *


def app(_):
    return Table(columns=columns, dataSource=data)
