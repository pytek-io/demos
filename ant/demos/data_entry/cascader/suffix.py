import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html

options = [
    {
        "value": "zhejiang",
        "label": "Zhejiang",
        "children": [
            {
                "value": "hangzhou",
                "label": "Hangzhou",
                "children": [{"value": "xihu", "label": "West Lake"}],
            }
        ],
    },
    {
        "value": "jiangsu",
        "label": "Jiangsu",
        "children": [
            {
                "value": "nanjing",
                "label": "Nanjing",
                "children": [{"value": "zhonghuamen", "label": "Zhong Hua Men"}],
            }
        ],
    },
]


def app():
    cascader1 = antd.Cascader(
        suffixIcon=ant_icons.SmileOutlined([]),
        options=options,
        placeholder="Please select",
    )
    cascader2 = antd.Cascader(
        suffixIcon="ab", options=options, placeholder="Please select"
    )
    cascader3 = antd.Cascader(
        expandIcon=ant_icons.SmileOutlined([]),
        options=options,
        placeholder="Please select",
    )
    cascader4 = antd.Cascader(
        expandIcon="ab", options=options, placeholder="Please select"
    )
    r.autorun(lambda: print("changed", cascader1()))
    r.autorun(lambda: print("changed", cascader2()))
    r.autorun(lambda: print("changed", cascader3()))
    r.autorun(lambda: print("changed", cascader4()))
    return html.div(
        [
            cascader1,
            html.br(),
            html.br(),
            cascader2,
            html.br(),
            html.br(),
            cascader3,
            html.br(),
            html.br(),
            cascader4,
        ]
    )
