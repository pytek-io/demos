import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Result(
        "Back Home",
        status="404",
        title="404",
        subTitle="Sorry, the page you visited does not exist.",
        extra=antd.Button(type="primary"),
    )
