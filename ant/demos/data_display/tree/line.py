import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html

treeData = [
    {
        "title": "parent 1",
        "key": "0-0",
        "icon": ant_icons.CarryOutOutlined(),
        "children": [
            {
                "title": "parent 1-0",
                "key": "0-0-0",
                "icon": ant_icons.CarryOutOutlined(),
                "children": [
                    {
                        "title": "leaf",
                        "key": "0-0-0-0",
                        "icon": ant_icons.CarryOutOutlined(),
                    },
                    {
                        "title": [
                            html.div("multiple line title"),
                            html.div("multiple line title"),
                        ],
                        "key": "0-0-0-1",
                        "icon": ant_icons.CarryOutOutlined(),
                    },
                    {
                        "title": "leaf",
                        "key": "0-0-0-2",
                        "icon": ant_icons.CarryOutOutlined(),
                    },
                ],
            },
            {
                "title": "parent 1-1",
                "key": "0-0-1",
                "icon": ant_icons.CarryOutOutlined(),
                "children": [
                    {
                        "title": "leaf",
                        "key": "0-0-1-0",
                        "icon": ant_icons.CarryOutOutlined(),
                    }
                ],
            },
            {
                "title": "parent 1-2",
                "key": "0-0-2",
                "icon": ant_icons.CarryOutOutlined(),
                "children": [
                    {
                        "title": "leaf",
                        "key": "0-0-2-0",
                        "icon": ant_icons.CarryOutOutlined(),
                    },
                    {
                        "title": "leaf",
                        "key": "0-0-2-1",
                        "icon": ant_icons.CarryOutOutlined(),
                        # switcher"icon": <FormOutlined />,
                    },
                ],
            },
        ],
    },
    {
        "title": "parent 2",
        "key": "0-1",
        "icon": ant_icons.CarryOutOutlined(),
        "children": [
            {
                "title": "parent 2-0",
                "key": "0-1-0",
                "icon": ant_icons.CarryOutOutlined(),
                "children": [
                    {
                        "title": "leaf",
                        "key": "0-1-0-0",
                        "icon": ant_icons.CarryOutOutlined(),
                    },
                    {
                        "title": "leaf",
                        "key": "0-1-0-1",
                        "icon": ant_icons.CarryOutOutlined(),
                    },
                ],
            },
        ],
    },
]


def app():
    show_line = antd.Switch()
    show_icon = antd.Switch()
    return html.div(
        [
            html.div(
                [
                    "show line:",
                    show_line,
                    html.br(),
                    html.br(),
                    "show icon:",
                    show_icon,
                    html.br(),
                    html.br(),
                ],
                style=dict(marginBottom=16),
            ),
            antd.Tree(
                showLine=show_line,
                showIcon=show_icon,
                defaultExpandedKeys=["0-0-0"],
                treeData=treeData,
            ),
        ]
    )
