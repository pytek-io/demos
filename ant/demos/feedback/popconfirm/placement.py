from reflect_html import *
from reflect_antd import Popconfirm, message, Button


def app():
    text = "Are you sure to delete this task?"

    def confirm():
        message.info("Clicked on Yes.")

    return div(
        [
            div(
                [
                    Popconfirm(
                        Button("TL"),
                        placement="topLeft",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    Popconfirm(
                        Button("Top"),
                        placement="top",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    Popconfirm(
                        Button("TR"),
                        placement="topRight",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                ],
                style=dict(marginLeft=70, whiteSpace="nowrap"),
            ),
            div(
                [
                    Popconfirm(
                        Button("LT"),
                        placement="leftTop",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    Popconfirm(
                        Button("Left"),
                        placement="left",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    Popconfirm(
                        Button("LB"),
                        placement="leftBottom",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                ],
                style=dict(width=70, float="left"),
            ),
            div(
                [
                    Popconfirm(
                        Button("RT"),
                        placement="rightTop",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    Popconfirm(
                        Button("Right"),
                        placement="right",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    Popconfirm(
                        Button("RB"),
                        placement="rightBottom",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                ],
                style=dict(width=70, marginLeft=304),
            ),
            div(
                [
                    Popconfirm(
                        Button("BL"),
                        placement="bottomLeft",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    Popconfirm(
                        Button("Bottom"),
                        placement="bottom",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                    Popconfirm(
                        Button("BR"),
                        placement="bottomRight",
                        title=text,
                        onConfirm=confirm,
                        okText="Yes",
                        cancelText="No",
                    ),
                ],
                style=dict(marginLeft=70, clear="both", whiteSpace="nowrap"),
            ),
        ],
        className="demo",
    )
