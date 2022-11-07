from reflect_html import *
from reflect_antd import Tag, Divider


def app():
    return div(
        [
            Divider("Presets Inverse", orientation="left"),
            div(
                [
                    Tag("magenta", color="magenta-inverse"),
                    Tag("red", color="red-inverse"),
                    Tag("volcano", color="volcano-inverse"),
                    Tag("orange", color="orange-inverse"),
                    Tag("gold", color="gold-inverse"),
                    Tag("lime", color="lime-inverse"),
                    Tag("green", color="green-inverse"),
                    Tag("cyan", color="cyan-inverse"),
                    Tag("blue", color="blue-inverse"),
                    Tag("geekblue", color="geekblue-inverse"),
                    Tag("purple", color="purple-inverse"),
                ]
            ),
        ]
    )
