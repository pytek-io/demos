from reflect_html import *
from reflect_antd import Cascader

from reflect import autorun

options = [
    {
        "code": "zhejiang",
        "name": "Zhejiang",
        "items": [
            {
                "code": "hangzhou",
                "name": "Hangzhou",
                "items": [{"code": "xihu", "name": "West Lake"}],
            }
        ],
    },
    {
        "code": "jiangsu",
        "name": "Jiangsu",
        "items": [
            {
                "code": "nanjing",
                "name": "Nanjing",
                "items": [{"code": "zhonghuamen", "name": "Zhong Hua Men"}],
            }
        ],
    },
]


def app():
    cascader = Cascader(
        fieldNames=dict(label="name", value="code", children="items"),
        options=options,
        placeholder="Please select",
    )
    autorun(lambda: print("changed", cascader()))
    return cascader