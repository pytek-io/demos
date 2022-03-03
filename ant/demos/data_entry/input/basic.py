from reflect_html import *
from reflect_antd import Input

from reflect import autorun

def app():
    text_input =  Input(placeholder="Basic usage")
    autorun(lambda : print(text_input()))
    return text_input