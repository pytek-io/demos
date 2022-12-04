import reflect_antd as antd
import reflect_html as html

Panel = antd.Collapse.Panel


def app():
    text = """
A dog is a type of domesticated animal.
Known for its loyalty and faithfulness,
it can be found as a welcome guest in many households across the world.
"""
    return antd.Space(
        [
            antd.Collapse(
                Panel(
                    html.p(text),
                    header="This panel can only be collapsed by clicking text",
                    key="1",
                ),
                collapsible="header",
                defaultActiveKey=["1"],
            ),
            antd.Collapse(
                Panel(html.p(text), header="This panel can't be collapsed", key="1"),
                collapsible="disabled",
            ),
        ],
        direction="vertical",
    )
