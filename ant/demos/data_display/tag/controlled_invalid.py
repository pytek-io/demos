from render_html import *
from render_antd import Tag, Button
def app():
    return[
 Tag("Movies", closable=True, visible=this.state.visible, onClose=lambda :this.setState( visible: false )),
 br(),
 Button("Toggle", size="small", onClick=lambda :this.setState( visible: !this.state.visible )),
]
def app():
    return Demo()