from reflect_rcdock import DockLayout
from reflect_html import img
from itertools import count


def create_content(file_name):
    return {
        "title": file_name,
        "content": img(
            src="website/static/react.svg",
            alt="react",
            style={
                "maxWidth": "100%",
                "maxHeight": "100%",
                "width": "auto",
                "height": "auto",
            },
        ),
    }


def app():
    counter = count(1)
    defaultLayout = {
        "dockbox": {
            "mode": "horizontal",
            "children": [
                {
                    "mode": "vertical",
                    "children": [
                        {
                            "tabs": [create_content(f"tab {next(counter)}")],
                        }
                        for i in range(2)
                    ]
                    + [
                        {
                            "tabs": [create_content(f"tab {next(counter)}")],
                        }
                    ],
                },
                {
                    "tabs": [create_content(f"tab {next(counter)}")],
                },
            ],
        }
    }
    return DockLayout(
        defaultLayout=defaultLayout,
        style={
            "width": "100%",
            "height": "50vh", # this is needed to show up properly when embedded in md doc
        },
    )
