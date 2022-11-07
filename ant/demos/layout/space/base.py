import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Space(
        [
            "Space",
            antd.Button("Button", type="primary"),
            antd.Upload(antd.Button([ant_icons.UploadOutlined(), "Click to Upload"])),
            antd.Popconfirm(
                antd.Button("Confirm"),
                title="Are you sure delete this task?",
                okText="Yes",
                cancelText="No",
            ),
        ]
    )
