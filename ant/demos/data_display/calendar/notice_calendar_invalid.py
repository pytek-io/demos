from render_antd import Badge, Calendar
from render_html import *


def app(_):
    return ul([""{listData.map(item => (", li(Badge(status=item.type, text=item.content), key=item.content), "))}""], className="events")
def app(_):
    return Calendar(dateCellRender=dateCellRender, monthCellRender=monthCellRender)