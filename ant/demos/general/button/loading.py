import asyncio

import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app(_):
    loadings = [r.ObservableValue(False) for i in range(3)]

    def enter_loading(loading):
        async def result():
            loading.set(True)
            await asyncio.sleep(3)
            loading.set(False)

        return result

    return html.div(
        [
            antd.Button("Loading", type="primary", loading=True),
            antd.Button("Loading", type="primary", size="small", loading=True),
            antd.Button(
                type="primary", icon=ant_icons.PoweroffOutlined(), loading=True
            ),
            html.br(),
            antd.Button(
                "Click me!",
                type="primary",
                loading=loadings[0],
                onClick=enter_loading(loadings[0]),
            ),
            antd.Button(
                "Click me!",
                type="primary",
                icon=ant_icons.PoweroffOutlined(),
                loading=loadings[1],
                onClick=enter_loading(loadings[1]),
            ),
            antd.Button(
                type="primary",
                icon=ant_icons.PoweroffOutlined(),
                loading=loadings[2],
                onClick=enter_loading(loadings[2]),
            ),
        ]
    )
