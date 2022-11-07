import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            html.p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
            antd.Divider("Text"),
            html.p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
            antd.Divider("Left Text", orientation="left"),
            html.p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
            antd.Divider("Right Text", orientation="right"),
            html.p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
        ]
    )
