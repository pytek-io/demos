import render as r
import render_antd as antd
import render_html as html


def app(_):
    current = r.ObservableValue(0)

    def onChange(current_value):
        print("onChange:", current_value)
        current.set(current_value)

    return html.div(
        [
            antd.Steps(
                items=[
                    {
                        "title": "Step 1",
                        "subTitle": "00:00:05",
                        "status": "finish",
                        "description": "This is a description.",
                    },
                    {
                        "title": "Step 2",
                        "subTitle": "00:01:02",
                        "status": "process",
                        "description": "This is a description.",
                    },
                    {
                        "title": "Step 3",
                        "subTitle": "waiting for a long long time",
                        "status": "wait",
                        "description": "This is a description.",
                    },
                ],
                type="navigation",
                size="small",
                current=current,
                onChange=onChange,
                className="site-navigation-steps",
            ),
            antd.Steps(
                items=[
                    {"status": "finish", "title": "Step 1"},
                    {"status": "process", "title": "Step 2"},
                    {"status": "wait", "title": "Step 3"},
                    {"status": "wait", "title": "Step 4"},
                ],
                type="navigation",
                current=current,
                onChange=onChange,
                className="site-navigation-steps",
            ),
            antd.Steps(
                items=[
                    {"status": "finish", "title": "finish 1"},
                    {"status": "finish", "title": "finish 2"},
                    {"status": "process", "title": "current process"},
                    {"status": "wait", "title": "wait", "disabled": True},
                ],
                type="navigation",
                size="small",
                current=current,
                onChange=onChange,
                className="site-navigation-steps",
            ),
        ]
    )
