import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Upload(
        antd.Button("Upload Directory", icon=ant_icons.UploadOutlined([])),
        action="https://www.mocky.io/v2/5cc8019d300000980a055e76",
        directory=True,
    )
