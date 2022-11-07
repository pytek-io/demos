import itertools

import reflect_html as html
import reflect_rcdock as rcdock


def create_content(file_name):
    return {
        "title": file_name,
        "content": html.img(
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
    counter = itertools.count(1)
    defaultLayout = {
        "dockbox": {
            "mode": "horizontal",
            "children": [
                {
                    "mode": "vertical",
                    "children": [
                        {"tabs": [create_content(f"tab {next(counter)}")]}
                        for i in range(2)
                    ]
                    + [{"tabs": [create_content(f"tab {next(counter)}")]}],
                },
                {"tabs": [create_content(f"tab {next(counter)}")]},
            ],
        }
    }
    return rcdock.DockLayout(
        defaultLayout=defaultLayout, style={"width": "100%", "height": "50vh"}
    )
