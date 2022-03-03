from reflect_html import *
from reflect_antd import Button
from reflect_ant_icons import PoweroffOutlined
from reflect import make_observable
import asyncio


def app():
    loadings = [make_observable(False) for i in range(3)]

    def enter_loading(loading):
        async def result():
            loading.set(True)
            await asyncio.sleep(3)
            loading.set(False)

        return result

    return [
        Button("Loading", type="primary", loading=True),
        Button("Loading", type="primary", size="small", loading=True),
        Button(type="primary", icon=PoweroffOutlined(), loading=True),
        br(),
        Button(
            "Click me!",
            type="primary",
            loading=loadings[0],
            onClick=enter_loading(loadings[0]),
        ),
        Button(
            "Click me!",
            type="primary",
            icon=PoweroffOutlined(),
            loading=loadings[1],
            onClick=enter_loading(loadings[1]),
        ),
        Button(
            type="primary",
            icon=PoweroffOutlined(),
            loading=loadings[2],
            onClick=enter_loading(loadings[2]),
        ),
    ]
