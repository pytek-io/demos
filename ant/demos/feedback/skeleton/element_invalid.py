from reflect_html import *
from reflect_antd import Skeleton, Space, Divider, Switch, Form, Radio

active, size, buttonShape, avatarShape = (
    this.active,
    this.size,
    this.buttonShape,
    this.avatarShape,
)


def app():
    return [
        Space(
            [
                Skeleton.Button(active=active, size=size, shape=buttonShape),
                Skeleton.Button(active=active, size=size, shape=buttonShape),
                Skeleton.Avatar(active=active, size=size, shape=avatarShape),
                Skeleton.Input(style=dict(width=200), active=active, size=size),
            ]
        ),
        br(),
        br(),
        Skeleton.Image(),
        Divider(),
        Form(
            [
                Form.Item(
                    Switch(checked=active, onChange=this.handleActiveChange),
                    label="Active",
                ),
                Form.Item(
                    Radio.Group(
                        [
                            Radio.Button("Default", value="default"),
                            Radio.Button("Large", value="large"),
                            Radio.Button("Small", value="small"),
                        ],
                        value=size,
                        onChange=this.handleSizeChange,
                    ),
                    label="Size",
                ),
                Form.Item(
                    Radio.Group(
                        [
                            Radio.Button("Default", value="default"),
                            Radio.Button("Round", value="round"),
                            Radio.Button("Circle", value="circle"),
                        ],
                        value=buttonShape,
                        onChange=this.handleShapeChange("buttonShape"),
                    ),
                    label="Button Shape",
                ),
                Form.Item(
                    Radio.Group(
                        [
                            Radio.Button("Square", value="square"),
                            Radio.Button("Circle", value="circle"),
                        ],
                        value=avatarShape,
                        onChange=this.handleShapeChange("avatarShape"),
                    ),
                    label="Avatar Shape",
                ),
            ],
            layout="inline",
            style=dict(margin="16px 0"),
        ),
    ]


def app():
    return Demo()
