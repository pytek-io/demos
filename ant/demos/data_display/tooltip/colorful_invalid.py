from render_antd import Button, Divider, Tooltip
from render_html import *


def app():
    return[
 Divider("Presets", orientation="left"),
 div([""{colors.map(color => (", Tooltip(Button(""{color}""), title="prompt text", color=color, key=color), "))}""]),
 Divider("Custom", orientation="left"),
 div([""{customColors.map(color => (", Tooltip(Button(""{color}""), title="prompt text", color=color, key=color), "))}""]),
]