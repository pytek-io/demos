from render_antd import Button, message
from render_html import *

info = Context.Provider([""{contextHolder}"", Button("Display normal message", type="primary", onClick=info)], value=dict(name='Ant Design'))
def app(_):
    return Demo()