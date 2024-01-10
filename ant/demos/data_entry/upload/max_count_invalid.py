import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app(_):
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
