import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html
import render_utils


def app(_):
    percent = r.ObservableValue(0)
    r.autorun(lambda: print("percent", percent()))
    return antd.Flex(
        [
            antd.Progress(type="circle", percent=percent),
            antd.Button.Group(
                [
                    antd.Button(
                        onClick=render_utils.increment_observable_bounded(
                            percent, 0, 100, -10
                        ),
                        icon=ant_icons.MinusOutlined([]),
                    ),
                    antd.Button(
                        onClick=render_utils.increment_observable_bounded(
                            percent, 0, 100, 10
                        ),
                        icon=ant_icons.PlusOutlined([]),
                    ),
                ]
            ),
        ],
        vertical=True,
        gap="small",
    )
