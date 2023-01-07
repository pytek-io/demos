import reflect as r
import reflect_antd as antd
import reflect_html as html
import random


def create_result(query, engine):
    number = random.randint(10, 100)
    category = f"{query}-{number}"
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
            style={
                "display": "flex",
                "justifyContent": "space-between",
            },
        ),
    }


def app():
    options_obs = r.ObservableList()

    def on_search(query: str):
        options_obs.set(
            [create_result(query, engine) for engine in ["google", "bing","yahoo"]]
        )

    return antd.AutoComplete(
        dropdownMatchSelectWidth=252,
        style=dict(width=300),
        options=options_obs,
        onSearch=r.Callback(on_search),
    )
