from reflect_html import *
from reflect_antd import Tag, Divider


def app():
    return div(
        [
            Divider("Presets", orientation="left"),
            div(
                [
                    Tag("magenta", color="magenta"),
                    Tag("red", color="red"),
                    Tag("volcano", color="volcano"),
                    Tag("orange", color="orange"),
                    Tag("gold", color="gold"),
                    Tag("lime", color="lime"),
                    Tag("green", color="green"),
                    Tag("cyan", color="cyan"),
                    Tag("blue", color="blue"),
                    Tag("geekblue", color="geekblue"),
                    Tag("purple", color="purple"),
                ]
            ),
            Divider("Custom", orientation="left"),
            div(
                [
                    Tag("#f50", color="#f50"),
                    Tag("#2db7f5", color="#2db7f5"),
                    Tag("#87d068", color="#87d068"),
                    Tag("#108ee9", color="#108ee9"),
                ]
            ),
        ]
    )
