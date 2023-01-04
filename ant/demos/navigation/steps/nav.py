import reflect_antd as antd
import reflect_html as html

import reflect as r


def app():
    current = r.ObservableValue(0)

    def onChange(current_value):
        print("onChange:", current_value)
        current.set(current_value)

    return html.div(
        [
            antd.Steps(
                items=[
                    {
                        "label": "Step 1",
                        "subTitle": "00:00:05",
                        "status": "finish",
                        "description": "This is a description.",
                    },
                    {
                        "label": "Step 2",
                        "subTitle": "00:01:02",
                        "status": "process",
                        "description": "This is a description.",
                    },
                    {
                        "label": "Step 3",
                        "subTitle": "waiting for longlong time",
                        "status": "wait",
                        "description": "This is a description.",
                    },
                ],
                type="navigation",
                size="small",
                current=current,
                onChange=r.Callback(onChange),
                className="site-navigation-steps",
            ),
            antd.Steps(
                items=[
                    {"status": "finish", "label": "Step 1"},
                    {"status": "process", "label": "Step 2"},
                    {"status": "wait", "label": "Step 3"},
                    {"status": "wait", "label": "Step 4"},
                ],
                type="navigation",
                current=current,
                onChange=r.Callback(onChange),
                className="site-navigation-steps",
            ),
            antd.Steps(
                items=[
                    {"status": "finish", "label": "finish 1"},
                    {"status": "finish", "label": "finish 2"},
                    {"status": "process", "label": "current process"},
                    {"status": "wait", "label": "wait", "disabled": True},
                ],
                type="navigation",
                size="small",
                current=current,
                onChange=r.Callback(onChange),
                className="site-navigation-steps",
            ),
        ]
    )
