import render_antd as antd
import render_html as html
import render as r

justifyOptions = [
    "flex-start",
    "center",
    "flex-end",
    "space-between",
    "space-around",
    "space-evenly",
]
alignOptions = ["flex-start", "center", "flex-end"]
boxStyle = {
    "width": "100%",
    "height": 120,
    "borderRadius": 6,
    "border": "1px solid #40a9ff",
}


def app():
    justify = antd.Segmented(options=justifyOptions)
    align = antd.Segmented(options=alignOptions)
    return antd.Flex(
        [
            html.p("Select justify:"),
            justify,
            html.p("Select align:"),
            align,
            antd.Flex(
                [
                    antd.Button("Primary", type="primary"),
                    antd.Button("Primary", type="primary"),
                    antd.Button("Primary", type="primary"),
                    antd.Button("Primary", type="primary"),
                ],
                style=boxStyle,
                justify=justify,
                align=align,
            ),
        ],
        gap="middle",
        vertical=True,
    )
