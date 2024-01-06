import render_antd as antd
import render_html as html


def app():
    text = "Are you sure to delete this task?"

    def confirm():
        antd.message.info("Clicked on Yes.")

    return html.div(
        [
            html.div(
                [
                    antd.Popconfirm(
                        antd.Button("TL"),
                        placement="topLeft",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    antd.Popconfirm(
                        antd.Button("Top"),
                        placement="top",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    antd.Popconfirm(
                        antd.Button("TR"),
                        placement="topRight",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                ],
                style={"marginLeft": 70, "whiteSpace": "nowrap"},
            ),
            html.div(
                [
                    antd.Popconfirm(
                        antd.Button("LT"),
                        placement="leftTop",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    antd.Popconfirm(
                        antd.Button("Left"),
                        placement="left",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    antd.Popconfirm(
                        antd.Button("LB"),
                        placement="leftBottom",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                ],
                style={"width": 70, "float": "left"},
            ),
            html.div(
                [
                    antd.Popconfirm(
                        antd.Button("RT"),
                        placement="rightTop",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    antd.Popconfirm(
                        antd.Button("Right"),
                        placement="right",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    antd.Popconfirm(
                        antd.Button("RB"),
                        placement="rightBottom",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                ],
                style={"width": 70, "marginLeft": 304},
            ),
            html.div(
                [
                    antd.Popconfirm(
                        antd.Button("BL"),
                        placement="bottomLeft",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    antd.Popconfirm(
                        antd.Button("Bottom"),
                        placement="bottom",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    antd.Popconfirm(
                        antd.Button("BR"),
                        placement="bottomRight",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                ],
                style={"marginLeft": 70, "clear": "both", "whiteSpace": "nowrap"},
            ),
        ],
        className="demo",
    )
