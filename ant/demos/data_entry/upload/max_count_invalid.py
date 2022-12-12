import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Space(
        [
            antd.Upload(
                antd.Button("Upload (Max: 1)", icon=ant_icons.UploadOutlined([])),
                action="https://www.mocky.io/v2/5cc8019d300000980a055e76",
                listType="picture",
                maxCount=1,
            ),
            antd.Upload(
                antd.Button("Upload (Max: 3)", icon=ant_icons.UploadOutlined([])),
                action="https://www.mocky.io/v2/5cc8019d300000980a055e76",
                listType="picture",
                maxCount=3,
                multiple=True,
            ),
        ],
        direction="vertical",
        style=dict(width="100%"),
        size="large",
    )
