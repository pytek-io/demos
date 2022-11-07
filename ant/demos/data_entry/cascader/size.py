from reflect_html import *
from reflect_antd import Cascader

from reflect import autorun

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
    cascader1 = Cascader(size="large", options=options)
    cascader2 = Cascader(options=options)
    cascader3 = Cascader(size="small", options=options)
    autorun(lambda: print("changed", cascader1()))
    autorun(lambda: print("changed", cascader2()))
    autorun(lambda: print("changed", cascader3()))
    return div(
        [
            cascader1,
            br(),
            br(),
            cascader2,
            br(),
            br(),
            cascader3,
            br(),
            br(),
        ]
    )
