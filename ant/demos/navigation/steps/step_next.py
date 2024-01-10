import render as r
import render_antd as antd
import render_html as html
import render_utils

steps = [
    {"title": "First", "content": "First-content"},
    {"title": "Second", "content": "Second-content"},
    {"title": "Last", "content": "Last-content"},
]

content_style = {
    "lineHeight": '260px',
    "textAlign": 'center',
    # "color": token.colorTextTertiary,
    # "backgroundColor": token.colorFillAlter,
    # "borderRadius": token.borderRadiusLG,
    # "border": "`1px dashed ${token.colorBorder}`",
    "marginTop": 16,
  }

def app(_):
    current = r.ObservableValue(0)
    return antd.Space(
        [
            antd.Steps(
                items=[
                    {"key": item["title"], "title": item["title"]} for item in steps
                ],
                current=current,
            ),
            html.div(lambda: steps[current()]["content"], className="steps-content", style=content_style),
            antd.Space(
                [
                    antd.Button(
                        "Previous",
                        type="primary",
                        onClick=render_utils.increment_observable_bounded(
                            current, 0, len(steps) - 1, -1
                        ),
                    ),
                    antd.Button(
                        "Next",
                        type="primary",
                        onClick=render_utils.increment_observable_bounded(
                            current, 0, len(steps) - 1, 1
                        ),
                    ),
                    antd.Button(
                        "Done",
                        type="primary",
                        onClick=lambda: antd.message.success("Processing complete!"),
                    ),
                ],
                className="steps-action",
            ),
        ],
        direction="vertical",
    )
    return result
