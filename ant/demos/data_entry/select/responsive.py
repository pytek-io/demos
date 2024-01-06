import render as r
import render_antd as antd


def app():
    value = r.ObservableList(["a10", "c12", "h17", "j19", "k20"])
    r.autorun(lambda: print(value()))
    selectProps = {
        "mode": "multiple",
        "style": {"width": "100%"},
        "options": [
            {"label": f"{chr(i + ord('a'))}{i}", "value": i} for i in range(10, 36)
        ],
        "placeholder": "Select Item...",
        "maxTagCount": "responsive",
    }
    return antd.Space(
        [
            antd.Select(value=value, **selectProps),
            antd.Select(disabled=True, **selectProps),
        ],
        direction="vertical",
        style={"width": "100%"},
    )
