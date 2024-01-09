from render_ant_icons import PlusOutlined
from render_antd import Modal, Upload
from render_html import *

previewVisible, previewImage, fileList, previewTitle = this.previewVisible, this.previewImage, this.fileList, this.previewTitle
uploadButton = div([PlusOutlined(), div("Upload", style=dict(marginTop=8))])
def app():
    return[
 Upload(""{fileList.length >= 8 ? null : uploadButton}"", action="https://www.mocky.io/v2/5cc8019d300000980a055e76", listType="picture-card", fileList=fileList, onPreview=this.handlePreview, onChange=this.handleChange),
 Modal(img(alt="example", style=dict(width='100%'), src=previewImage), visible=previewVisible, title=previewTitle, footer=null, onCancel=this.handleCancel),
]
def app():
    return PicturesWall()