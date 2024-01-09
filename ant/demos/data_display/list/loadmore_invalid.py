from render_antd import Avatar, Button, Divider, List, Skeleton
from render_html import *


def app():
    raise NotImplementedError("low level effect not supported")
    return [
        Divider("Default Size", orientation="left"),
        List(
            header=div("Header"), footer=div("Footer"), bordered=True, dataSource=data
        ),
        Divider("Small Size", orientation="left"),
        List(
            size="small",
            header=div("Header"),
            footer=div("Footer"),
            bordered=True,
            dataSource=data,
        ),
        Divider("Large Size", orientation="left"),
        List(
            size="large",
            header=div("Header"),
            footer=div("Footer"),
            bordered=True,
            dataSource=data,
        ),
    ]
