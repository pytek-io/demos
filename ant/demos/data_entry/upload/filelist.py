import render_ant_icons as ant_icons
import render_antd as antd


def app(_):
    return antd.Upload(antd.Button("Upload", icon=ant_icons.UploadOutlined()))
