from reflect_html import *
from reflect_antd import Form, Input, Button, Radio, Space
from reflect import Callback


def app():
    # def formItemLayout():
    #     return (
    #         {
    #             "labelCol": {"span": 4},
    #             "wrapperCol": {"span": 14},
    #         }
    #         if formLayout() == "horizontal"
    #         else {}
    #     )
    formLayout = Radio.Group(
        [
            Radio.Button("Horizontal", value="horizontal"),
            Radio.Button("Vertical", value="vertical"),
            Radio.Button("Inline", value="inline"),
        ],
    )

    def wrapperCol():
        return {"span": 14, "offset": 4} if formLayout() == "horizontal" else None

    initialValues = {"a": "A.", "b": "B."}
    return Space(
        [
            formLayout,
            Form(
                [
                    Form.Item(
                        Input(placeholder="input placeholder"),
                        label="Field A",
                        name="a",
                    ),
                    Form.Item(
                        Input(placeholder="input placeholder"),
                        label="Field B",
                        name="b",
                    ),
                    Form.Item(
                        Button("Submit", type="primary", htmlType="submit"),
                        wrapperCol=wrapperCol,
                    ),
                ],
                initialValues=initialValues,
                layout=formLayout,
                onValuesChange=Callback(
                    lambda values: print("values changed to", values)
                ),
            ),
        ],
        direction="vertical",
    )
