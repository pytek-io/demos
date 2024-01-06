import render_antd as antd
import render_html as html

import render as r


def app():
    percent = r.create_observable(0, key="percent")
    current = r.create_observable(1, key="current")
    status = r.create_observable("process", key="status")

    def increase():
        current.set(current() + 1)
        percent.set(0)

    return html.div(
        [
            antd.Button("Percentage to undefined", onClick=lambda: percent.set(None)),
            antd.Button(
                "Percentage +", onClick=lambda: percent.set((percent() + 10) % 100)
            ),
            antd.Button("Current +", onClick=increase),
            antd.Button("Status Wait", onClick=lambda: status.set("wait")),
            antd.Button("Status Process", onClick=lambda: status.set("process")),
            antd.Button("Status Finish", onClick=lambda: status.set("finish")),
            antd.Button("Status Error", onClick=lambda: status.set("error")),
            antd.Steps(
                [
                    Step(title="Finished", description="This is a description."),
                    Step(
                        title="In Progress",
                        subTitle="Left 00:00:08",
                        description="This is a description.",
                    ),
                    Step(title="Waiting", description="This is a description."),
                ],
                current=current,
                percent=percent,
                status=status,
            ),
            antd.Steps(
                [
                    Step(title="Finished", description="This is a description."),
                    Step(
                        title="In Progress",
                        subTitle="Left 00:00:08",
                        description="This is a description.",
                    ),
                    Step(title="Waiting", description="This is a description."),
                ],
                current=current,
                percent=percent,
                status=status,
                size="small",
            ),
            antd.Steps(
                [
                    Step(title="Finished", description="This is a description."),
                    Step(
                        title="In Progress",
                        subTitle="Left 00:00:08",
                        description="This is a description.",
                    ),
                    Step(title="Waiting", description="This is a description."),
                ],
                current=current,
                percent=percent,
                status=status,
                direction="vertical",
            ),
            antd.Steps(
                [
                    Step(title="Finished", description="This is a description."),
                    Step(
                        title="In Progress",
                        subTitle="Left 00:00:08",
                        description="This is a description.",
                    ),
                    Step(title="Waiting", description="This is a description."),
                ],
                current=current,
                percent=percent,
                status=status,
                size="small",
                direction="vertical",
            ),
        ]
    )
