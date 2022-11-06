from reflect_html import *
from reflect_antd import Input, Space
from reflect_ant_icons import EyeInvisibleOutlined, EyeTwoTone
def app():
    return Space([Input.Password(placeholder="input password"), Input.Password(placeholder="input password", iconRender=visibllambda e:(visible ? <EyeTwoTone /> : <EyeInvisibleOutlined />))], direction="vertical")