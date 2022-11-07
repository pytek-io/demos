import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Result(
        "Back Home",
        status="500",
        title="500",
        subTitle="Sorry, something went wrong.",
        extra=antd.Button(type="primary"),
    )
