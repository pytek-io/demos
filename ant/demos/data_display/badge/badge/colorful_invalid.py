from reflect_html import *
from reflect_antd import Badge, Divider
def app():
    return[
 Divider("Presets", orientation="left"),
 div([""{colors.map(color => (", div(Badge(color=color, text=color), key=color), "))}""]),
 Divider("Custom", orientation="left"),
 div([Badge(color="#f50", text="#f50"), br(), Badge(color="#2db7f5", text="#2db7f5"), br(), Badge(color="#87d068", text="#87d068"), br(), Badge(color="#108ee9", text="#108ee9")]),
]