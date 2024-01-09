from render_antd import Button, Tag
from render_html import *


def app():
    return[
 Tag("Movies", closable=True, visible=this.state.visible, onClose=lambda :this.setState( visible: false )),
 br(),
 Button("Toggle", size="small", onClick=lambda :this.setState( visible: !this.state.visible )),
]
def app():
    return Demo()