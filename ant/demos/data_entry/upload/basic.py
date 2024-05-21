import render_ant_icons as ant_icons
import render_antd as antd
import render as r


def app(_):
    result = antd.Upload(
        antd.Button(
            "Click to Upload",
            icon=ant_icons.UploadOutlined([]),
        ),
        name="file",
    )
    r.autoprint(result)
    return result
