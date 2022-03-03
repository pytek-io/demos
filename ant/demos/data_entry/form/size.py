from reflect_html import *
from reflect_antd import (
    Form,
    Input,
    Button,
    Cascader,
    Switch,
    Select,
    Radio,
    Space,
    TreeSelect,
    DatePicker,
    InputNumber,
)

def app():
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
    componentSize = Radio.Group(
        [
            Radio.Button("Small", value="small"),
            Radio.Button("Default", value="default"),
            Radio.Button("Large", value="large"),
        ]
    )
    return Space(
        [
            componentSize,
            Form(
                [
                    Form.Item(Input(), label="Input"),
                    Form.Item(
                        Select(Select.Option("Demo", value="demo")), label="Select"
                    ),
                    Form.Item(TreeSelect(treeData=treeData), label="TreeSelect"),
                    Form.Item(Cascader(options=options), label="Cascader"),
                    Form.Item(DatePicker(), label="DatePicker"),
                    Form.Item(InputNumber(), label="InputNumber"),
                    Form.Item(Switch(), label="Switch"),
                    Form.Item(Button("Button"), label="Button"),
                ],
                labelCol=dict(span=4),
                wrapperCol=dict(span=14),
                layout="horizontal",
                size=componentSize,
            ),
        ], direction="vertical"
    )
