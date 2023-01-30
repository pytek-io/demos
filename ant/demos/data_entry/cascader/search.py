import reflect as r
import reflect_antd as antd


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

filterCascaderSearch = r.JSMethod(
    "filterCascaderSearch",
    """
      return path.some(
        (option) =>
          option.label.toLowerCase().indexOf(inputValue.toLowerCase()) > -1
      );
    """,
    "inputValue",
    "path",
)


def app():
    cascader = antd.Cascader(
        options=options,
        placeholder="Please select",
        showSearch=filterCascaderSearch,
    )
    r.autoprint(cascader)
    return cascader
