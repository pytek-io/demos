import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html
import reflect_utils


def app():
    percent = r.create_observable(0)
    r.autorun(lambda: print("percent", percent()))
    return html.div(
        [
            antd.Progress(type="circle", percent=percent),
            antd.Button.Group(
                [
                    antd.Button(
                        onClick=reflect_utils.increment_observable_bounded(
                            percent, 0, 100, -10
                        ),
                        icon=ant_icons.MinusOutlined([]),
                    ),
                    antd.Button(
                        onClick=reflect_utils.increment_observable_bounded(
                            percent, 0, 100, 10
                        ),
                        icon=ant_icons.PlusOutlined([]),
                    ),
                ]
            ),
        ]
    )
