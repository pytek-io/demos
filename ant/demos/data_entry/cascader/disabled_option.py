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
        "disabled": True,
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
    result = antd.Cascader(options=options)
    r.autorun(lambda: print(result()))
    return result
