import reflect as r
import reflect_antd as antd
import reflect_html as html

Panel = antd.Collapse.Panel


collapse_expand_icon = r.js_arrow(
    "collapse_renderer",
    "({isActive}) => reflect_ant_icons.CaretRightOutlined([], { rotate: (isActive ? 90 : 0)});",
    ["reflect_ant_icons"]
)


def app():
    text = """
A dog is a type of domesticated animal.
Known for its loyalty and faithfulness,
it can be found as a welcome guest in many households across the world.
"""
    return antd.Collapse(
        [
            Panel(
                html.p(text),
                header="This is panel header 1",
                key="1",
                className="site-collapse-custom-panel",
            ),
            Panel(
                html.p(text),
                header="This is panel header 2",
                key="2",
                className="site-collapse-custom-panel",
            ),
            Panel(
                html.p(text),
                header="This is panel header 3",
                key="3",
                className="site-collapse-custom-panel",
            ),
        ],
        bordered=False,
        defaultActiveKey=["1"],
        expandIcon=collapse_expand_icon,
    )
