from render_html import *
from render_antd import Space, Slider, Button
def app():
    return[
 Slider(value=size, onChange=valulambda e:setSize(value)),
 br(),
 br(),
 Space([Button("Primary", type="primary"), Button("Default"), Button("Dashed", type="dashed"), Button("Link", type="link")], size=size),
]
def app():
    return SpaceCustomizeSize()