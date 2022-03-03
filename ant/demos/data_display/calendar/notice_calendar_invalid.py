from reflect_html import *
from reflect_antd import Calendar, Badge
def app():
    return ul([""{listData.map(item => (", li(Badge(status=item.type, text=item.content), key=item.content), "))}""], className="events")
def app():
    return Calendar(dateCellRender=dateCellRender, monthCellRender=monthCellRender)