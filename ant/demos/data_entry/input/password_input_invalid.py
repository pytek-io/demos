from render_html import *
from render_antd import Input, Space
from render_ant_icons import EyeInvisibleOutlined, EyeTwoTone
def app():
    return Space([Input.Password(placeholder="input password"), Input.Password(placeholder="input password", iconRender=visibllambda e:(visible ? <EyeTwoTone /> : <EyeInvisibleOutlined />))], direction="vertical")