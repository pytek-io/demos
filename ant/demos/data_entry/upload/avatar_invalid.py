from render_html import *
from render_antd import Upload, message
from render_ant_icons import LoadingOutlined, PlusOutlined
loading, imageUrl = this.loading, this.imageUrl
uploadButton = div([""{loading ?", LoadingOutlined(), ":", PlusOutlined(), "}"", div("Upload", style=dict(marginTop=8))])
def app():
    return Upload([""{imageUrl ?", img(src=imageUrl, alt="avatar", style=dict(width='100%')), ": uploadButton}""], name="avatar", listType="picture-card", className="avatar-uploader", showUploadList=False, action="https://www.mocky.io/v2/5cc8019d300000980a055e76", beforeUpload=beforeUpload, onChange=this.handleChange)
def app():
    return Avatar()