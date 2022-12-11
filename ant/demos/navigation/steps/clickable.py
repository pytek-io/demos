import reflect_antd as antd
import reflect_html as html

import reflect as r


def app():
    current = r.create_observable(0)

    def onChange(value):
        print("onChange:", current)
        current.set(value)

    return html.div(
        [
            antd.Steps(
                items=[
                    {"label": "Step 1", "description": "This is a description."},
                    {"label": "Step 2", "description": "This is a description."},
                    {"label": "Step 3", "description": "This is a description."},
                ],
                current=current,
                onChange=r.Callback(onChange),
            ),
            antd.Divider(),
            antd.Steps(
                items=[
                    {"label": "Step 1", "description": "This is a description."},
                    {"label": "Step 2", "description": "This is a description."},
                    {"label": "Step 3", "description": "This is a description."},
                ],
                current=current,
                onChange=r.Callback(onChange),
                direction="vertical",
            ),
        ]
    )
