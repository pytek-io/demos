from reflect_html import *
from reflect_antd import Tag, Input, Tooltip
from reflect_ant_icons import PlusOutlined
inputValue = this.inputValue
tags, inputVisible, inputValue, editInputIndex, editInputValue = this.tags, this.inputVisible, this.inputValue, this.editInputIndex, this.editInputValue
def app():
    return Input(ref=this.saveEditInputRef, key=tag, size="small", className="tag-input", value=editInputValue, onChange=this.handleEditInputChange, onBlur=this.handleEditInputConfirm, onPressEnter=this.handleEditInputConfirm)
tagElem = Tag(span(""{isLongTag ? `$"{tag.slice(0, 20)}"...` : tag}"", onDoubleClick="{lambda e:", {=True, if=True, (index=True, !="0)", "{=True, this.setState(=True, editInputIndex:=True, index,=True, editInputValue:=True, tag=True, }",=True, lambda=True, :"{=True, this.editInput.focus();=True, );=True, e.preventDefault();=True, }"=True, !}"=True), className="edit-tag", key=tag, closable=index !== 0, onClose=lambda :this.handleClose(tag))
def app():
    return EditableTagGroup()