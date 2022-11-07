from reflect_html import *
from reflect_antd import Divider


def app():
    return div(
        [
            p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
            Divider("Text", plain=True),
            p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
            Divider("Left Text", orientation="left", plain=True),
            p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
            Divider("Right Text", orientation="right", plain=True),
            p(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista       probare, quae sunt a te dicta? Refert tamen, quo modo."
            ),
        ]
    )
