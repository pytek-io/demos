from render_antd import Affix, Button
from render_html import *


def app():
    return Affix(Button("120px to affix top"), offsetTop=120, onChange=affixed => print(affixed))