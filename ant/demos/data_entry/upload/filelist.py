import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Upload(antd.Button("Upload", icon=ant_icons.UploadOutlined()))
