from reflect_html import *
from reflect_antd import Upload, Button, Tooltip
from reflected.react.dnd import DndProvider, useDrag, useDrop, createDndContext
from reflected.react.dnd.html5.backend import HTML5Backend
from reflect_ant_icons import UploadOutlined
index: dragIndex = monitor.index: dragIndex
errorNode = Tooltip(""{originNode.props.children}"", title="Upload Error", getPopupContainer=lambda :document.body)
def app():
    return div(""{file.status === 'error' ? errorNode : originNode}"", ref=ref, className="{`ant-upload-draggable-list-item $", {isOver=True, ?=True, dropClassName=True, :=True, ''}"`}"=True, style=dict(cursor='move'))
onChange = DndProvider([Upload(action="https://www.mocky.io/v2/5cc8019d300000980a055e76", fileList=fileList, onChange=onChange, itemRender="{(originNode, file, currFileList) => (           <DragableUploadListItem             originNode=", {originNode}"=True, file=file, fileList=currFileList, moveRow=moveRow), ")}"       >", Button([UploadOutlined(), "Click to Upload"])], manager=manager.current.dragDropManager)
def app():
    return DragSortingUpload()