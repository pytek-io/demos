import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    open_obs = r.ObservableValue(True)
    close = lambda: open_obs.set(False)
    placement = antd.Radio.Group(
                        options=[
                            {"value": "top", "label": "Top"},
                            {"value": "right", "label": "Right"},
                            {"value": "bottom", "label": "Bottom"},
                            {"value": "left", "label": "Left"},
                        ],
                    )
    return html.div(
        [
            antd.Space(
                [
                    placement,
                    antd.Button(
                        "Open", type="primary", onClick=lambda: open_obs.set(True)
                    ),
                ]
            ),
            antd.Drawer(
                [
                    html.p("Some content..."),
                    html.p("Some content..."),
                    html.p("Some content..."),
                ],
                title="Drawer with extra actions",
                placement=placement,
                width=500,
                onClose=close,
                open=open_obs,
                extra=antd.Space([
                    antd.Button("Cancel", onClick=close),
                    antd.Button("OK", onClick=close)
                ])
            ),
        ]
    )
