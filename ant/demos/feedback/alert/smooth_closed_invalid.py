from render_antd import Alert
from render_html import *

handleClose = div([""{visible ? (", Alert(message="Alert Message Text", type="success", closable=True, afterClose=handleClose), ") : null}"", p("placeholder text here")])
def app():
    return App()