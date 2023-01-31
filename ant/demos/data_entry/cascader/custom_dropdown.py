import reflect as r
import reflect_antd as antd

# const handleAreaClick = (
#   e: React.MouseEvent<HTMLAnchorElement>,
#   label: string,
#   option: DefaultOptionType,
# ) => {
#   e.stopPropagation();
#   console.log('clicked', label, option);
# };

# const displayRender = (labels: string[], selectedOptions: DefaultOptionType[]) =>
#   labels.map((label, i) => {
#     const option = selectedOptions[i];
#     if (i === labels.length - 1) {
#       return (
#         <span key={option.value}>
#           {label} (<a onClick={(e) => handleAreaClick(e, label, option)}>{option.code}</a>)
#         </span>
#       );
#     }
#     return <span key={option.value}>{label} / </span>;
#   });

render_selection = r.js_arrow(
    "render_selection",
    """
(labels, selectedOptions) => {
  return labels.map((label, i) => {
    const option = selectedOptions[i];
    if (i === labels.length - 1) {
      return reflect_html.span(reflect_html.a(option.code), {
        key: option.value,
      });
    }
    return reflect_html.span(label, { key: option.value });
  });
};
""",
)

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
    return antd.Cascader(
        options=options,
        displayRender=render_selection,
        placeholder="Please select",
    )
