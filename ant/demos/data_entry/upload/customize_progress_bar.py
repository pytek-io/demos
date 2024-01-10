import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app(_):
    return antd.Upload(
        antd.Button("Click to Upload", icon=ant_icons.UploadOutlined([]))
    )
