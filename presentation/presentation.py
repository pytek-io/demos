TITLE = "Spectacle presentation"

from reflect_html import img, div
from reflect_spectacle import (
    Heading,
    Deck,
    Slide,
    FlexBox,
    UnorderedList,
    ListItem,
)
from reflect import js
from website.common import BACKGROUND_COLOR, FONT_FAMILY, LIGHT_BLUE, GREEN
from website.main import HTML_LINKS
from website.home import SLOGAN

BACKGROUND_COLOR = "rgb" + str(BACKGROUND_COLOR)
BODY_STYLE = {"backGroundColor": BACKGROUND_COLOR}


def title(content, color=LIGHT_BLUE, fontSize="60px"):
    return Heading(
        div(
            content,
            style={"color": color, "fontFamily": FONT_FAMILY},
        ),
        fontSize=fontSize,
        margin="0px",
    )


content = [
    [
        "Who are we?",
        "A startup building a Python enterprise framework called Reflect.",
    ],
    [
        "What do we mean by Python enterprise framework?",
        "A technology allowing to build web applications (aka web apps) all in Python",
    ],
    [
        "What is a web app?",
        "A web page which allows for user interaction (eg: web mail, social network pages, etc).",
    ],
    [
        "What are Reflect's advantages over existing solutions?",
        "Web apps require complex infrastructure, various programming languages, tools, etc. With Reflect the only thing you need to do is write (short) Python scripts.",
    ],
    [
        "In which situation can you use Reflect?",
        "Reflect is extremely well suited for building in house systems, and B2B portals, etc",
    ],
    [
        "Are there any examples of apps build on top of Reflect?",
        "You can see a few in the website app demos section. Our website and even this presentation are build with Reflect (we eat our own dog food and we love it!).",
    ],
    [
        "Which industry would benefit most from Reflect?",
        "Finance is the most obvious, but no mean the only one, industry, services, etc. Any organization which need an efficient solution to build systems in Python.",
    ],
    ["What is our goal?", "Expand our user community to the professional world. Gather users feedback while helping them to get a better understanding of their needs."],
    [
        "Which users are we targeting?",
        "Any startup, small company that has a business need for Reflect.",
    ],
    [
        "How much does Reflect cost?",
        "Nothing, Reflect is free to use for the time being. Early adopters will have the right to use their copy indefinitely.",
    ],
    [
        "How do you get started?",
        "You can download Reflect and start using it straightaway. Please feel to reach out to us we will be more than happy to guide your first steps!",
    ],
    [
        "Anything else we want you to know?",
        "Reflect is in beta, meaning we won't change its interface. We are aiming for the prod release mid year. We are also working hard on improving the tutorial, demos, so stay tuned.",
    ],
]

import itertools


def roman_numeral(number):
    if number <= 3:
        return "I" * number
    if number == 4:
        return "IV"
    if number >= 5:
        return "V" + roman_numeral(number - 5)


def grouper(n, iterable):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


def app():
    pytek = img(
        alt="pytek logo",
        src="website/static/cogs_pytek.svg",
        style={
            "height": 200,
        },
    )

    theme = {
        "colors": {"primary": LIGHT_BLUE, "secondary": GREEN},
        "fontSizes": {"header": "64px", "paragraph": "28px"},
    }

    slides = [
        Slide(
            FlexBox(
                [
                    title(pytek, fontSize="72px"),
                    title(SLOGAN, LIGHT_BLUE),
                    img(
        alt="dashboard",
        src="demos/dashboard/default.png",
        style={
            "height": 200,
        },
    ),
                    div(
                        "Early adopters presentation",
                        style={
                            "fontFamily": FONT_FAMILY,
                            "color":GREEN,
                            "fontSize": "50px",
                        },
                    ),
                ],
                flexDirection="column",
            ),
            backgroundColor=BACKGROUND_COLOR,
        )
    ]
    slides.extend(
        Slide(
            [
                title(f"Quick fire questions and answers {roman_numeral(index)}"),
                UnorderedList(
                    itertools.chain.from_iterable(
                        (
                            ListItem(
                                div(
                                    question,
                                    style={
                                        "fontFamily": FONT_FAMILY,
                                    },
                                ),
                                color=GREEN,
                            ),
                            ListItem(
                                div(
                                    answer,
                                    style={
                                        "marginRight": "10px",
                                        "fontSize": "30px",
                                        "borderColor": GREEN,
                                        "borderStyle": "dashed",
                                        "padding": 10,
                                        "display": "inline-block",
                                    },
                                ),
                            ),
                        )
                        for question, answer in items
                    )
                ),
            ],
            backgroundColor=BACKGROUND_COLOR,
        )
        for index, (items) in enumerate(grouper(3, content), 1)
    )
    return Deck(
        slides,
        template=js("presentation_template"),
        theme=theme,
    )
