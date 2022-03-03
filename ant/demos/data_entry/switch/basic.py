from reflect_html import *
from reflect_antd import Switch

from reflect import autorun

def app():
    switch = Switch(defaultChecked=True)
    autorun(lambda: print(f"switched to {switch()}"))
    return switch
