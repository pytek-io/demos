from reflect_html import *
from reflect_antd import Pagination
def app():
    return[
 Pagination(total=85, showTotal="{total => `Total $", {total}"=True, items`}"=True, defaultPageSize=20, defaultCurrent=1),
 br(),
 Pagination(total=85, showTotal="{(total, range) => `$", {range[0]}"-$"{range[1]}"=True, of=True, $"{total}"=True, items`}"=True, defaultPageSize=20, defaultCurrent=1),
]