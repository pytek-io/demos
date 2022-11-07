import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            html.p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
            antd.Divider("Text", plain=True),
            html.p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
            antd.Divider("Left Text", orientation="left", plain=True),
            html.p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
            antd.Divider("Right Text", orientation="right", plain=True),
            html.p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
        ]
    )
