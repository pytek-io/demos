from reflect_html import *
from reflect_antd import Button, notification, Divider, Space
def app():
    return Context.Provider([""{contextHolder}"", Space([Button([RadiusUpleftOutlined(), "topLeft"], type="primary", onClick=lambda :openNotification('topLeft')), Button([RadiusUprightOutlined(), "topRight"], type="primary", onClick=lambda :openNotification('topRight'))]), Divider(), Space([Button([RadiusBottomleftOutlined(), "bottomLeft"], type="primary", onClick=lambda :openNotification('bottomLeft')), Button([RadiusBottomrightOutlined(), "bottomRight"], type="primary", onClick=lambda :openNotification('bottomRight'))])], value=dict(name='Ant Design'))
def app():
    return Demo()