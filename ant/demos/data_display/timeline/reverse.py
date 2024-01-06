import render as r
import render_antd as antd
import render_html as html
import render_utils


def app():
    reverse = r.ObservableValue(False)
    return html.div(
        [
            antd.Timeline(
                items=[
                    {
                        "children": "Create a services site 2015-09-01",
                    },
                    {
                        "children": "Solve initial network problems 2015-09-01",
                    },
                    {
                        "children": "Technical testing 2015-09-01",
                    },
                ],
                pending="Recording...",
                reverse=reverse,
            ),
            antd.Button(
                "Toggle Reverse",
                type="primary",
                style={"marginTop": 16},
                onClick=render_utils.toggle_observable(reverse),
            ),
        ]
    )
