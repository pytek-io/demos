from reflect_antd import Typography

TITLE = "Spectacle presentation"

from reflect_antd import Row, Col
from reflect_html import img, span, div
from reflect_spectacle import (
    Heading,
    Deck,
    Slide,
    CodePane,
    FlexBox,
    UnorderedList,
    ListItem,
    CodeSpan,
)
from reflect import js


CSS = [
    "./website/ant_site_index.css",
    "./demos/ant_markdown.css",
    "./demos/ant_site_logo.css",
]

Title = Typography.Title

REACT_LOGO_ICON_PATH = (
    "https://gw.alipayobjects.com/zos/antfincdn/aPkFc8Sj7n/method-draw-image.svg"
)

PYTHON_LOGO_ICON_PATH = (
    "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
)

py_code = """[
    Button("Primary Button", type="primary"),
    Button("Default Button"),
    Button("Dashed Button", type="dashed"),
]"""

js_code = """<>
    <Button type="primary">Primary Button</Button>
    <Button>Default Button</Button>
    <Button type="dashed">Dashed Button</Button>
</>"""


def app():
    react = img(
        alt="logo",
        src=REACT_LOGO_ICON_PATH,
        width=300,
    )
    python = img(
        alt="logo",
        src=PYTHON_LOGO_ICON_PATH,
        width=300,
    )

    def logos():
        return div(
            [react, span("+", style=dict(margin="20px", fontSize="150px")), python],
            className="pic-plus",
        )

    color = "#006400"
    theme = {
        "colors": {"primary": color, "secondary": color},
        "fontSizes": {"header": "64px", "paragraph": "28px"},
    }
    slides = [
        Slide(
            FlexBox(
                [
                    Heading("Reflect", color="primary", margin="0px", fontSize="150px"),
                    Heading(logos()),
                ],
                flexDirection="column",
            ),
            backgroundColor="black",
        ),
        Slide(
            [
                Heading("What is Python?", color="primary", margin="0px"),
                UnorderedList(
                    [
                        ListItem(
                            CodeSpan(
                                "The most popular high level programming language."
                            )
                        ),
                        ListItem(
                            CodeSpan(
                                "Thanks to its instrinsic simplicity and huge ecosystem."
                            )
                        ),
                        ListItem(
                            CodeSpan(
                                "De facto the new standard in the financial industry among others."
                            )
                        ),
                    ]
                ),
            ],
            backgroundColor="black",
        ),
        Slide(
            [
                Heading(["What is React?"], color="primary", margin="0px"),
                UnorderedList(
                    [
                        ListItem(
                            CodeSpan("The most popular web interface technology.")
                        ),
                        ListItem(
                            CodeSpan(
                                "Extremely elegant design, huge ecosystem of libraries easily reusable."
                            )
                        ),
                        ListItem(
                            CodeSpan(
                                "De facto the standard in the web technology for building web application."
                            )
                        ),
                    ]
                ),
            ],
            backgroundColor="black",
        ),
        Slide(
            [
                Heading(["What's the deal?"], color="primary", margin="0px"),
                UnorderedList(
                    [
                        ListItem(
                            CodeSpan(
                                "Combining those two technologies together requires a significant amount of work."
                            )
                        ),
                        ListItem(
                            CodeSpan(
                                "The application state needs to be kept in sync between the client and the server."
                            )
                        ),
                        ListItem(
                            CodeSpan(
                                "Everyone ends up reinventing the exact same wheel..."
                            )
                        ),
                    ]
                ),
            ],
            backgroundColor="black",
        ),
        Slide(
            [
                Heading(["What solution do we offer?"], color="primary", margin="0px"),
                UnorderedList(
                    [
                        ListItem(
                            CodeSpan(
                                "A Python framework that exposes React components directly."
                            )
                        ),
                        ListItem(
                            CodeSpan(
                                "Powerful callback free API, most common libraries readily usable."
                            )
                        ),
                        ListItem(
                            CodeSpan(
                                "De facto the standard in the web technology for building web application."
                            )
                        ),
                    ]
                ),
            ],
            backgroundColor="black",
        ),
        Slide(
            [
                Heading(["What solution do we offer?"], color="primary", margin="0px"),
                Row(
                    [
                        Col(
                            [
                                Heading("JSX", fontSize="h3"),
                                CodePane(
                                    js_code,
                                    language="jsx",
                                ),
                            ],
                            span=12,
                            style=dict(overflow="hidden"),
                        ),
                        Col(
                            [
                                Heading("Python", fontSize="h3"),
                                CodePane(py_code, language="python"),
                            ],
                            span=12,
                            style=dict(overflow="hidden"),
                        ),
                    ],
                    gutter=30,
                ),
            ],
            backgroundColor="black",
        ),
    ]
    return div(
        [
            div("hello world"),
            Deck(
                slides,
                template=js("presentation_template"),
                theme=theme,
                style=dict(height="80%"),
            ),
        ]
    )
