from reflect_html import *
from reflect_antd import Steps, Button, Space
from reflect import create_observable
from reflect_utils import increment_observable_bounded


Step = Steps.Step

steps = [
    {
        "title": "First",
        "content": "First-content",
    },
    {
        "title": "Second",
        "content": "Second-content",
    },
    {
        "title": "Last",
        "content": "Last-content",
    },
]


def app():
    current = create_observable(0)
    return Space(
        [
            Steps(
                [Step(key=item["title"], title=item["title"]) for item in steps],
                current=current,
            ),
            # rmk: notice how we differ content evaluation to avoid recomputing the whole method
            div(
                lambda: steps[current()]["content"],
                className="steps-content",
            ),
            Space(
                [
                    Button(
                        "Previous",
                        type="primary",
                        onClick=increment_observable_bounded(current, 0, len(steps) - 1, -1),
                    ),
                    Button(
                        "Next",
                        type="primary",
                        onClick=increment_observable_bounded(current, 0, len(steps) - 1, 1),
                    ),
                    Button(
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