from render_ant_icons import PlusOutlined
from render_antd import Input, Tag
from render_html import *
from rendered.rc.tween.one import TweenOneGroup

inputValue = this.inputValue
tags, inputVisible, inputValue = this.tags, this.inputVisible, this.inputValue
tagElem = Tag(""{tag}"", closable=True, onClose="{lambda e:", {=True, e.preventDefault();=True, this.handleClose(tag);=True, !}"=True)
def app(_):
    return span(""{tagElem}"", key=tag, style=dict(display='inline-block'))
def app(_):
    return[
 div(TweenOneGroup(""{tagChild}"", enter="{!               scale: 0.8,               opacity: 0,               type: 'from',               duration: 100,               onComplete: lambda e:", {=True, e.target.style="", ;=True, }",=True, !}"=True, leave=dict(opacity=0, width=0, scale=0, duration=200), appear=False), style=dict(marginBottom=16)),
 Input(ref=this.saveInputRef, type="text", size="small", style=dict(width=78), value=inputValue, onChange=this.handleInputChange, onBlur=this.handleInputConfirm, onPressEnter=this.handleInputConfirm),
 Tag([PlusOutlined(), "New Tag"], onClick=this.showInput, className="site-tag-plus"),
]
def app(_):
    return EditableTagGroup()