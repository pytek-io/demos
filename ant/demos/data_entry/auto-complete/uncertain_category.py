import random

import render as r
import render_antd as antd
import render_html as html


def create_result(query, engine):
    number = random.randint(10, 100)
    category = f"{query} {engine}({number})"
    return {
        "value": category,
        "label": html.div(
            [
                html.span(
                    [
                        f"Found {query} on {engine} ",
                        html.a(
                            category,
                            href=f"https://www.{engine}.com/search?q={query}",
                            target="_blank",
                            rel="noopener noreferrer",
                        ),
                    ]
                ),
                html.span(number),
            ],
            style={"display": "flex", "justifyContent": "space-between"},
        ),
    }


def app():
    options_obs = r.ObservableList()

    def on_search(query: str):
        options_obs.set(
            [create_result(query, engine) for engine in ["google", "bing", "yahoo"]]
        )

    return antd.AutoComplete(
        dropdownMatchSelectWidth=252,
        style={"width": 300},
        options=options_obs,
        onSearch=on_search,
    )
