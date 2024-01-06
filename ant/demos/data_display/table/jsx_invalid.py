from render_html import *
from render_antd import Table, Tag, Space
Column, ColumnGroup = Table.Column, Table.ColumnGroup
def app():
    return Tag(""{tag}"", color="blue", key=tag)