import render_antd as antd


def app():
    formLayout = antd.Radio.Group(
        [
            antd.Radio.Button("Horizontal", value="horizontal"),
            antd.Radio.Button("Vertical", value="vertical"),
            antd.Radio.Button("Inline", value="inline"),
        ]
    )

    def wrapperCol():
        return {"span": 14, "offset": 4} if formLayout() == "horizontal" else None

    initialValues = {"a": "A.", "b": "B."}
    return antd.Space(
        [
            formLayout,
            antd.Form(
                [
                    antd.Form.Item(
                        antd.Input(placeholder="input placeholder"),
                        label="Field A",
                        name="a",
                    ),
                    antd.Form.Item(
                        antd.Input(placeholder="input placeholder"),
                        label="Field B",
                        name="b",
                    ),
                    antd.Form.Item(
                        antd.Button("Submit", type="primary", htmlType="submit"),
                        wrapperCol=wrapperCol,
                    ),
                ],
                initialValues=initialValues,
                layout=formLayout,
                onValuesChange=lambda values: print("values changed to", values),
            ),
        ],
        direction="vertical",
    )
