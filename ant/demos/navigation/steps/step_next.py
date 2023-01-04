import reflect_antd as antd
import reflect_html as html
import reflect_utils

import reflect as r

steps = [
    {"title": "First", "content": "First-content"},
    {"title": "Second", "content": "Second-content"},
    {"title": "Last", "content": "Last-content"},
]


def app():
    current = r.ObservableValue(0)
    return antd.Space(
        [
            antd.Steps(
                items=[
                    {"key": item["title"], "label": item["title"]} for item in steps
                ],
                current=current,
            ),
            html.div(lambda: steps[current()]["content"], className="steps-content"),
            antd.Space(
                [
                    antd.Button(
                        "Previous",
                        type="primary",
                        onClick=reflect_utils.increment_observable_bounded(
                            current, 0, len(steps) - 1, -1
                        ),
                    ),
                    antd.Button(
                        "Next",
                        type="primary",
                        onClick=reflect_utils.increment_observable_bounded(
                            current, 0, len(steps) - 1, 1
                        ),
                    ),
                    antd.Button(
                        "Done",
                        type="primary",
                        onClick=lambda: print("Processing complete!"),
                    ),
                ],
                className="steps-action",
            ),
        ],
        direction="vertical",
    )
    return result
