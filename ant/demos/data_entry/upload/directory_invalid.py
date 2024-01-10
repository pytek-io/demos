import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app(_):
    return antd.Upload(
        antd.Button("Upload Directory", icon=ant_icons.UploadOutlined([])),
        action="https://www.mocky.io/v2/5cc8019d300000980a055e76",
        directory=True,
    )
