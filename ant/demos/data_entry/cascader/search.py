import render as r
import render_antd as antd

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

filterCascaderSearch = r.js_arrow(
    "filterCascaderSearch",
    """
      (inputValue, path) => path.some(
        (option) =>
          option.label.toLowerCase().indexOf(inputValue.toLowerCase()) > -1
      );
    """,
)


def app(_):
    cascader = antd.Cascader(
        options=options,
        placeholder="Please select",
        showSearch=filterCascaderSearch,
    )
    r.autoprint(cascader)
    return cascader
