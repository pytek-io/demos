from reflect_html import *
from reflect_antd import Modal, Button
clientWidth, clientHeight = window.clientWidth, window.clientHeight
bounds, disabled, visible = this.bounds, this.disabled, this.visible
def app():
    return[
 Button("Open Draggable Modal", onClick=this.showModal),
 Modal("Draggable Modal", title="{             <div               style=", {!=True, width:=True, '100%',=True, cursor:=True, 'move',=True, !}"=True, onMouseOver="{lambda :", {=True, if=True, (disabled)=True, "{=True, this.setState(=True, disabled:=True, false,=True, );=True, }"=True, !}"=True, onMouseOut="{lambda :", {=True, this.setState(=True, disabled:=True, true,=True, );=True, !}"=True, fix=True, eslintjsx-a11y=True, mouse-events-have-key-events=True, https:=True, github.com=True, jsx-eslint=True, eslint-plugin-jsx-a11y=True, blob=True, master=True, docs=True, rules=True, mouse-events-have-key-events.md=True, onFocus="{lambda :", {!}"=True, onBlur="{lambda :", {!}"=True, end=True),
 Draggable(div(""{modal}"", ref=this.draggleRef), disabled=disabled, bounds=bounds, onStart=(event, uiData) => this.onStart(event, uiData)),
 p("Just don't learn physics at school and your life will be full of magic and             miracles."),
 br(),
 p("Day before yesterday I saw a rabbit, and yesterday a deer, and today, you."),
]
def app():
    return App()