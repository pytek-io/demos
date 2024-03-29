import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Tooltip(
                antd.Button(
                    type="primary", shape="circle", icon=ant_icons.SearchOutlined([])
                ),
                title="search",
            ),
            antd.Button("A", type="primary", shape="circle"),
            antd.Button("Search", type="primary", icon=ant_icons.SearchOutlined([])),
            antd.Tooltip(
                antd.Button(shape="circle", icon=ant_icons.SearchOutlined([])),
                title="search",
            ),
            antd.Button("Search", icon=ant_icons.SearchOutlined([])),
            html.br(),
            antd.Tooltip(
                antd.Button(shape="circle", icon=ant_icons.SearchOutlined([])),
                title="search",
            ),
            antd.Button("Search", icon=ant_icons.SearchOutlined([])),
            antd.Tooltip(
                antd.Button(
                    type="dashed", shape="circle", icon=ant_icons.SearchOutlined([])
                ),
                title="search",
            ),
            antd.Button("Search", type="dashed", icon=ant_icons.SearchOutlined([])),
        ]
    )
