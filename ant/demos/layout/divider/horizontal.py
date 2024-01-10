import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            html.p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
            antd.Divider(),
            html.p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
            antd.Divider(dashed=True),
            html.p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
        ]
    )
