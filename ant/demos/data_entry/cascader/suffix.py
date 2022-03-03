from reflect_html import *
from reflect_antd import Cascader
from reflect_ant_icons import SmileOutlined

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
    cascader1 = Cascader(
        suffixIcon=SmileOutlined([]),
        options=options,
        placeholder="Please select",
    )
    cascader2 = Cascader(
        suffixIcon="ab",
        options=options,
        placeholder="Please select",
    )
    cascader3 = Cascader(
        expandIcon=SmileOutlined([]),
        options=options,
        placeholder="Please select",
    )
    cascader4 = Cascader(
        expandIcon="ab",
        options=options,
        placeholder="Please select",
    )
    autorun(lambda: print("changed", cascader1()))
    autorun(lambda: print("changed", cascader2()))
    autorun(lambda: print("changed", cascader3()))
    autorun(lambda: print("changed", cascader4()))
    return [
        cascader1,
        br(),
        br(),
        cascader2,
        br(),
        br(),
        cascader3,
        br(),
        br(),
        cascader4,
    ]
