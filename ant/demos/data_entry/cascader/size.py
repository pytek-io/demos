import render as r
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
    cascader1 = antd.Cascader(size="large", options=options)
    cascader2 = antd.Cascader(options=options)
    cascader3 = antd.Cascader(size="small", options=options)
    r.autorun(lambda: print("changed", cascader1()))
    r.autorun(lambda: print("changed", cascader2()))
    r.autorun(lambda: print("changed", cascader3()))
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
        ]
    )
