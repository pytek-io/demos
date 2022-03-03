from reflect_html import *
from reflect_antd import message, Button
info = Context.Provider([""{contextHolder}"", Button("Display normal message", type="primary", onClick=info)], value=dict(name='Ant Design'))
def app():
    return Demo()