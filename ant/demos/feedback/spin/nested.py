import render as r
import render_antd as antd
import render_html as html


def app(_):
    loading = antd.Switch(defaultChecked=False)
    return html.div(
        [
            antd.Spin(
                antd.Alert(
                    message="Alert message title",
                    description="Further details about the context of this alert.",
                    type="info",
                ),
                spinning=loading,
            ),
            html.div(["Loading state：", loading], style={"marginTop": 16}),
        ]
    )
