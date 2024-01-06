from render_antd import Table
from render_html import *


def app():
    return Table(columns=columns, dataSource=data)
