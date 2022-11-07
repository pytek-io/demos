import reflect as r
import reflect_antd as antd
import reflect_html as html

Option, OptGroup = antd.Select.Option, antd.Select.OptGroup


def app():
    select = antd.Select(
        [
            OptGroup(
                [Option("Jack", value="jack"), Option("Lucy", value="lucy")],
                label="Manager",
            ),
            OptGroup(Option("yiminghe", value="Yiminghe"), label="Engineer"),
        ],
        defaultValue="lucy",
        style=dict(width=200),
    )
    r.autorun(lambda: print(select()))
    return select
