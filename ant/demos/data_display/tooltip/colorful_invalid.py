from render_html import *
from render_antd import Tooltip, Button, Divider
def app():
    return[
 Divider("Presets", orientation="left"),
 div([""{colors.map(color => (", Tooltip(Button(""{color}""), title="prompt text", color=color, key=color), "))}""]),
 Divider("Custom", orientation="left"),
 div([""{customColors.map(color => (", Tooltip(Button(""{color}""), title="prompt text", color=color, key=color), "))}""]),
]