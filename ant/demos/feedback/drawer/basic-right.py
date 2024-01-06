import render as r
import render_antd as antd
import render_html as html


def app():
    open_obs = r.ObservableValue(True)
    return html.div(
        [
            antd.Button("Open", type="primary"),
            antd.Drawer(
                [
                    html.p("Some content..."),
                    html.p("Some content..."),
                    html.p("Some content..."),
                ],
                title="Basic drawer",
                placement="right",
                onClose=lambda: open_obs.set(False),
                open=open_obs,
            ),
        ]
    )
