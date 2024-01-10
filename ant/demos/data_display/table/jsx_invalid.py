from render_antd import Space, Table, Tag
from render_html import *

Column, ColumnGroup = Table.Column, Table.ColumnGroup
def app(_):
    return Tag(""{tag}"", color="blue", key=tag)