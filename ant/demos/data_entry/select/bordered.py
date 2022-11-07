import reflect_antd as antd
import reflect_html as html

Option = antd.Select.Option


def app():
    return html.div(
        [
            antd.Select(
                [
                    Option("Jack", value="jack"),
                    Option("Lucy", value="lucy"),
                    Option("yiminghe", value="Yiminghe"),
                ],
                defaultValue="lucy",
                style=dict(width=120),
                bordered=False,
            ),
            antd.Select(
                Option("Lucy", value="lucy"),
                defaultValue="lucy",
                style=dict(width=120),
                disabled=True,
                bordered=False,
            ),
        ]
    )
