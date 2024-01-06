import render_ant_icons
import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Divider("Without icon", orientation="left"),
            html.div(
                [
                    antd.Tag("success", color="success"),
                    antd.Tag("processing", color="processing"),
                    antd.Tag("error", color="error"),
                    antd.Tag("warning", color="warning"),
                    antd.Tag("default", color="default"),
                ]
            ),
            antd.Divider("With icon", orientation="left"),
            html.div(
                [
                    antd.Tag(
                        "success",
                        icon=render_ant_icons.CheckCircleOutlined(),
                        color="success",
                    ),
                    antd.Tag(
                        "processing",
                        icon=render_ant_icons.SyncOutlined("spin"),
                        color="processing",
                    ),
                    antd.Tag(
                        "error",
                        icon=render_ant_icons.CloseCircleOutlined(),
                        color="error",
                    ),
                    antd.Tag(
                        "warning",
                        icon=render_ant_icons.ExclamationCircleOutlined(),
                        color="warning",
                    ),
                    antd.Tag(
                        "waiting",
                        icon=render_ant_icons.ClockCircleOutlined(),
                        color="default",
                    ),
                    antd.Tag(
                        "stop",
                        icon=render_ant_icons.MinusCircleOutlined(),
                        color="default",
                    ),
                ]
            ),
        ]
    )
