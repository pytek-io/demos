import reflect as r
import reflect_antd as antd
import reflect_html as html

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
    cascader = antd.Cascader(
        fieldNames=dict(label="name", value="code", children="items"),
        options=options,
        placeholder="Please select",
    )
    r.autorun(lambda: print("changed", cascader()))
    return cascader
