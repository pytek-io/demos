from reflect_antd import Select, Space
from reflect_html import *

from reflect import autorun, create_observable


def app():
    value = create_observable(["a10", "c12", "h17", "j19", "k20"])
    autorun(lambda: print(value()))
    selectProps = {
        "mode": "multiple",
        "style": {"width": "100%"},
        "defaultValue": value,
        "options": [
            {"label": f"{chr(i + ord('a'))}{i}", "value": i} for i in range(10, 36)
        ],
        "placeholder": "Select Item...",
        "maxTagCount": "responsive",
    }
    return Space(
        [Select(value=value, **selectProps), Select(disabled=True, **selectProps)],
        direction="vertical",
        style=dict(width="100%"),
    )
