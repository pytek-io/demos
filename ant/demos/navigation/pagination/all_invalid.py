from reflect_html import *
from reflect_antd import Pagination
def app():
    return Pagination(total=85, showSizeChanger=True, showQuickJumper=True, showTotal="{total => `Total $", {total}"=True, items`}"=True)