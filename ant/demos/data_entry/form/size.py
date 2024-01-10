import render_antd as antd


def app(_):
    treeData = [
        {
            "title": "Light",
            "value": "light",
            "children": [{"title": "Bamboo", "value": "bamboo"}],
        }
    ]
    options = [
        {
            "value": "zhejiang",
            "label": "Zhejiang",
            "children": [{"value": "hangzhou", "label": "Hangzhou"}],
        }
    ]
    componentSize = antd.Radio.Group(
        [
            antd.Radio.Button("Small", value="small"),
            antd.Radio.Button("Default", value="default"),
            antd.Radio.Button("Large", value="large"),
        ]
    )
    return antd.Space(
        [
            componentSize,
            antd.Form(
                [
                    antd.Form.Item(antd.Input(), label="Input"),
                    antd.Form.Item(
                        antd.Select(options=[{"label": "Demo", "value": "demo"}]),
                        label="Select",
                    ),
                    antd.Form.Item(
                        antd.TreeSelect(treeData=treeData), label="TreeSelect"
                    ),
                    antd.Form.Item(antd.Cascader(options=options), label="Cascader"),
                    antd.Form.Item(antd.DatePicker(), label="DatePicker"),
                    antd.Form.Item(antd.InputNumber(), label="InputNumber"),
                    antd.Form.Item(antd.Switch(), label="Switch"),
                    antd.Form.Item(antd.Button("Button"), label="Button"),
                ],
                labelCol={"span": 4},
                wrapperCol={"span": 14},
                layout="horizontal",
                size=componentSize,
            ),
        ],
        direction="vertical",
    )
