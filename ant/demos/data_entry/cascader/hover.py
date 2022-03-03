from reflect_html import *
from reflect_antd import Cascader
from reflect import js
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
    cascader = Cascader(
        options=options,
        expandTrigger="hover",
        displayRender=js("cascaderHoverDisplayRender"),
    )
    autorun(lambda: print(cascader()))
    return cascader
