from reflect_html import *
from reflect_antd import Table


def app():
    return Table(columns=columns, dataSource=data)
