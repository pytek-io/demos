import reflect_antd as antd
import reflect_html as html

Step = antd.Steps.Step


def app():
    return antd.Steps(
        [Step(title="Finished"), Step(title="In Progress"), Step(title="Waiting")],
        size="small",
        current=1,
    )
