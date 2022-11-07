import reflect as r
import reflect_antd as antd
import reflect_html as html

Option = antd.Select.Option


def app():
    select = antd.Select(
        [
            Option("Jack", value="jack"),
            Option("Lucy", value="lucy"),
            Option("Disabled", value="disabled", disabled=True),
            Option("yiminghe", value="Yiminghe"),
        ],
        defaultValue="lucy",
        style=dict(width=120),
    )
    r.autorun(lambda: print("selected", select()))
    return html.div(
        [
            select,
            antd.Select(
                Option("Lucy", value="lucy"),
                defaultValue="lucy",
                style=dict(width=120),
                disabled=True,
            ),
            antd.Select(
                Option("Lucy", value="lucy"),
                defaultValue="lucy",
                style=dict(width=120),
                loading=True,
            ),
            antd.Select(
                Option("Lucy", value="lucy"),
                defaultValue="lucy",
                style=dict(width=120),
                allowClear=True,
            ),
        ]
    )
