from render_antd import Divider, Radio, Table
from render_html import *


def app():
    return div([Radio.Group([""{           setSelectionType(value);         !}"         value="{selectionType}"       >", Radio("Checkbox", value="checkbox"), Radio("radio", value="radio")], onChange="{( target: ", {=True, value=True, }"=True, )=""), Divider(), Table(rowSelection=dict(type=selectionType), columns=columns, dataSource=data)])
def app():
    return Demo()