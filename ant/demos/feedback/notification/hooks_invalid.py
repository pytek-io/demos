from render_antd import Button, Divider, Space, notification
from render_html import *


def app(_):
    return Context.Provider([""{contextHolder}"", Space([Button([RadiusUpleftOutlined(), "topLeft"], type="primary", onClick=lambda :openNotification('topLeft')), Button([RadiusUprightOutlined(), "topRight"], type="primary", onClick=lambda :openNotification('topRight'))]), Divider(), Space([Button([RadiusBottomleftOutlined(), "bottomLeft"], type="primary", onClick=lambda :openNotification('bottomLeft')), Button([RadiusBottomrightOutlined(), "bottomRight"], type="primary", onClick=lambda :openNotification('bottomRight'))])], value=dict(name='Ant Design'))
def app(_):
    return Demo()