from reflect_html import *
from reflect_antd import Steps, Button
from reflect import create_observable, Callback

Step = Steps.Step


def app():
    percent = create_observable(0, key="percent")
    current = create_observable(1, key="current")
    status = create_observable("process", key="status")

    def increase():
        current.set((current() + 1))
        percent.set(0)

    return div([
        Button("Percentage to undefined", onClick=lambda: percent.set(None)),
        Button(
            "Percentage +", onClick=lambda: percent.set((percent() + 10) % 100)
        ),
        Button("Current +", onClick=increase),
        Button("Status Wait", onClick=lambda: status.set("wait")),
        Button("Status Process", onClick=lambda: status.set("process")),
        Button("Status Finish", onClick=lambda: status.set("finish")),
        Button("Status Error", onClick=lambda: status.set("error")),
        Steps(
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
        Steps(
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
        Steps(
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
        Steps(
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
    ])
