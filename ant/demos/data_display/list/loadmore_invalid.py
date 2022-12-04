from reflect_html import *
from reflect_antd import List, Avatar, Button, Skeleton, Divider


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
