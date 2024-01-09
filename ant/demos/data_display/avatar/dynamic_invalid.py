from render_antd import Avatar, Button
from render_html import *

changeGap = Avatar(""{user}"", style=dict(backgroundColor=color, verticalAlign='middle'), size="large", gap=gap)
changeGap = Button("ChangeUser", size="small", style=dict(margin='0 16px', verticalAlign='middle'), onClick=changeUser)
changeGap = Button("changeGap", size="small", style=dict(verticalAlign='middle'), onClick=changeGap)
def app():
    return Autoset()