import reflect_antd as antd
import reflect_html as html

Step = antd.Steps.Step


def app():
    return antd.Steps(
        [
            Step(title="Finished", description="This is a description"),
            Step(title="In Process", description="This is a description"),
            Step(title="Waiting", description="This is a description"),
        ],
        current=1,
        status="error",
    )
