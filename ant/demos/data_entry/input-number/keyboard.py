from reflect_html import *
from reflect_antd import InputNumber, Button, Switch


def app():
    switch = Switch("Toggle keyboard")
    return [InputNumber(min=1, max=10, keyboard=switch, defaultValue=3), switch]
