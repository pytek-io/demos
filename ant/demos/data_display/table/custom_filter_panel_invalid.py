from render_html import *
from render_antd import Table, Input, Button, Space
from render_ant_icons import SearchOutlined

data = [
    {
        "key": "1",
        "name": "John Brown",
        "age": 32,
        "address": "New York No. 1 Lake Park",
    },
    {"key": "2", "name": "Joe Black", "age": 42, "address": "London No. 1 Lake Park"},
    {"key": "3", "name": "Jim Green", "age": 32, "address": "Sidney No. 1 Lake Park"},
    {"key": "4", "name": "Jim Red", "age": 32, "address": "London No. 2 Lake Park"},
]
    

def app():
    return App()
