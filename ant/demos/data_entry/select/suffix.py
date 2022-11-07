import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

Option = antd.Select.Option


def app():
    smileIcon = ant_icons.SmileOutlined()
    mehIcon = ant_icons.MehOutlined()
    select = antd.Select(
        [
            Option("Jack", value="jack"),
            Option("Lucy", value="lucy"),
            Option("Disabled", value="disabled", disabled=True),
            Option("yiminghe", value="Yiminghe"),
        ],
        suffixIcon=smileIcon,
        defaultValue="lucy",
        style=dict(width=120),
    )
    r.autorun(lambda: print("selected", select()))
    return html.div(
        [
            select,
            antd.Select(
                Option("Lucy", value="lucy"),
                suffixIcon=mehIcon,
                defaultValue="lucy",
                style=dict(width=120),
                disabled=True,
            ),
        ]
    )
