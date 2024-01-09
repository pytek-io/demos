from render_antd import Button, Skeleton
from render_html import *


def app():
    return div(
        [
            Skeleton(
                div(
                    [
                        h4("Ant Design, a design language"),
                        p(
                            "We supply a series of design principles, practical patterns and high quality design               resources (Sketch and Axure), to help people create their product prototypes               beautifully and efficiently."
                        ),
                    ]
                ),
                loading=this.state.loading,
            ),
            Button(
                "Show Skeleton", onClick=this.showSkeleton, disabled=this.state.loading
            ),
        ],
        className="article",
    )


def app():
    return Demo()
