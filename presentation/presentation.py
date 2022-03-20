TITLE = "Early adopters presentation"
from reflect import get_window, make_observable, ResponsiveValue
from reflect_html import img, div, svg, path, a
from website.common import BACKGROUND_COLOR, FONT_FAMILY, LIGHT_BLUE, GREEN
from website.main import HTML_LINKS
from website.home import SLOGAN
from functools import partial
from reflect_swiper import Swiper, SwiperSlide
from website.reflect.gallery import MENU as GALLERY_MENU

import itertools
import os

RIGHT_ARROW = 39
LEFT_ARROW = 37
LOGO_HEIGHT = 52
HOME_PAGE = "website.home"

maximize = "M396.795 396.8H320V448h128V320h-51.205zM396.8 115.205V192H448V64H320v51.205zM115.205 115.2H192V64H64v128h51.205zM115.2 396.795V320H64v128h128v-51.205z"

minimize = "M64 371.2h76.795V448H192V320H64v51.2zm76.795-230.4H64V192h128V64h-51.205v76.8zM320 448h51.2v-76.8H448V320H320v128zm51.2-307.2V64H320v128h128v-51.2h-76.8z"


BODY_STYLE = {"backgroundColor": "rgb" + str(BACKGROUND_COLOR), "fontSize": 10}
CSS = ["test.css"]


def select_file_extension(file_path):
    for extension in ["gif", "png", "svg", "jpg"]:
        maybe_path = f"{file_path}.{extension}"
        if os.path.exists(maybe_path):
            return maybe_path


def title(content, color=LIGHT_BLUE, fontSize="40px"):
    return div(
        content,
        style={
            "color": color,
            "fontFamily": FONT_FAMILY,
            "fontSize": fontSize,
            "textAlign": "center",
            "margin": fontSize,
        },
    )


def add_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d.items())
    return result


content = [
    [
        "Who are we?",
        "A startup building a Python enterprise framework called Reflect.",
        "Francois du Vignaud has launched the project in November 2021 with the help of a couple friends and ex colleagues. We strongly believe that we can provide a value          have very ambitious goals for the near future."
    ],
    [
        "What do we mean by Python enterprise framework?",
        "A technology allowing to build web applications (aka web apps) all in Python.",
        "Python has established itself as the most popular programming language after three decades of existence. Beyond scientific applications it is an extremely efficient programming language thanks to its user friendliness and humongous ecosystem of libraries. But despite all this there isn't any standard enterprise framework making for building enterprise system."
    ],
    [
        "What is a web app?",
        "A web page which allows for user interaction (eg: web mail, social network pages, etc).",
        "Put it another way a web app is a page which depends on the current context be it user inputs, realtime data, etc."
    ],
    [
        "What are Reflect's advantages over existing solutions?",
        "Web apps require complex infrastructure, various programming languages, tools, etc. With Reflect the only thing you need to do is write (short) Python scripts.",
        "The equivalent solutions to Reflect are either NodeJS and MS Blazer but for the fact that they rely on JavaScript and .Net respectively. Short of that one has to build a significant amount of technical infrastructure which usually comprise a front end part writtent in JS and a back-end part written in the target language. Building this is a challenging engineering issue which is usually completely uncorrelated with the actual business."
    ],
    [
        "In which situation can you use Reflect?",
        "Reflect is very well suited for building in house systems, and B2B portals, etc",
        "Given the architectural choices Reflect makes building such apps extremely easy. Any mildly experience Python can build a web app in a couple of hours. Deploying and maintaining is fully automated, making the overall development process perfectly seameless."
    ],
    [
        "Are there any examples of apps build on top of Reflect?",
        "You can see a few in the website app demos section. Our website and even this presentation are build with Reflect (we eat our own dog food and we love it!).",
        "We are building prototypes for a few startups already, some of them should be made public soon."
    ],
    [
        "Which industry would benefit most from Reflect?",
        "Finance is the most obvious, but no mean the only one, industry, services, etc. Any organization which need an efficient solution to build systems in Python.",
        ""
    ],
    [
        "What is our goal?",
        "Expand our user community to the professional world. Gather users feedback while helping them to get a better understanding of their needs.",
    ],
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


def create_icon(
    path_d, style={}, fill="currentColor", width=15, height=15, onClick=None
):
    return svg(
        path(d=path_d),
        viewBox="0 0 512 512",
        width=width,
        height=height,
        fill=fill,
        style=style,
        onClick=onClick,
    )


STYLE = {
    "position": "absolute",
    "bottom": "10px",
}


def left_center_right(left, center, right):
    return div(
        [
            div(left, style={"float": "left"}),
            div(right, style={"float": "right"}),
            div(center, style={"margin": "0 auto", "width": "fit-content"}),
        ],
        style={"width": "100%"},
    )


def create_bullet(color="white", transparent=True, onClick=None):
    STYLE = {
        "width": "10px",
        "height": "10px",
        "display": "inline-block",
        "border": "1px solid " + color,
        "background": "transparent" if transparent else color,
        "margin": "3.33333px",
        "borderRadius": "50%",
        "pointerEvents": "all",
        "cursor": "pointer",
    }
    return div(None, size=10, style=STYLE, onClick=onClick)


def app():
    window = get_window()
    full_screen = make_observable(False)

    def page_index():
        return int(window.hash()) if window.hash() else 0

    def set_page_index(index):
        window.hash.set(str(index))

    def safe_increment(increment):
        nonlocal page_index, set_page_index
        page_index_value = page_index()
        if increment:
            if page_index_value + 1 < len(slides):
                set_page_index(page_index_value + 1)
        else:
            if page_index_value > 0:
                set_page_index(page_index_value - 1)

    window.add_event_listener(
        "fullscreenchange",
        None,
        callback_name=None,
        method=lambda: full_screen.set(not full_screen()),
    )
    window.add_event_listener(
        "swiped", "detail.dir", lambda d: safe_increment(d == "right")
    )
    window.add_event_listener(
        "keydown",
        "keyCode",
        lambda k: k in (RIGHT_ARROW, LEFT_ARROW) and safe_increment(k == RIGHT_ARROW),
    )
    image = Swiper(
        [
            SwiperSlide(
                [
                    img(
                        dataSrc=select_file_extension(
                            os.path.join(
                                os.path.split(app_path.split("#")[0])[0], "default"
                            )
                        ),
                        style={"width": "100%"},
                        className="swiper-lazy",
                    ),
                    div(className="swiper-lazy-preloader-white"),
                ]
            )
            for name, app_path in GALLERY_MENU[:-1]  # excluding presentation
        ],
        navigation=True,
        style={
            "width": "50%",
        },
    )

    main_page = div(
        [
            title(SLOGAN, LIGHT_BLUE),
            image,
            title(
                "Early adopters presentation",
                color=GREEN,
                fontSize="3rem",
            ),
        ],
    )

    slides = [main_page] + [
        div(
            # [title(f"Rapid fire questions and answers {roman_numeral(index)}")]
            # +
            list(
                itertools.chain.from_iterable(
                    (
                        div(
                            question,
                            style={
                                "fontFamily": FONT_FAMILY,
                                "color": GREEN,
                                "fontSize": "2rem",
                                "padding": 10,
                            },
                        ),
                        div(
                            answer,
                            style={
                                "marginRight": "10px",
                                "marginBottom": "20px",
                                "fontSize": "2rem",
                                "color": LIGHT_BLUE,
                                "borderColor": GREEN,
                                "borderStyle": "dashed",
                                "padding": 10,
                                "display": "inline-block",
                                "width": "100%",
                            },
                        ),
                    )
                    for question, answer in items
                )
            ),
        )
        for index, items in enumerate(grouper(3, content), 1)
    ]

    def update_full_screen():
        window.update_full_screen(not full_screen())

    icon = create_icon(
        lambda: minimize if full_screen() else maximize,
        fill="white",
        width="2.5vh",
        height="2.5vh",
        style={
            "pointerEvents": "all",
            "cursor": "pointer",
        },
        onClick=update_full_screen,
    )

    def create_bullets():
        page_index_value = page_index()
        return [
            create_bullet(
                transparent=page_index_value != index,
                color="white",
                onClick=partial(set_page_index, index),
            )
            for index in range(len(slides))
        ]

    bottom = div(
        left_center_right(
            icon,
            create_bullet(transparent=True, color="white"),
            create_bullets,
        ),
        style={
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "center",
            "height": "100%",
            "marginLeft": "2rem",
            "marginRight": "2rem",
        },
    )

    def responsive_margins(content, style):
        margin = ResponsiveValue(
            xs=10, sm="10vh", md="10vh", lg=None, xl=None, xxl="20vh"
        )
        return div(
            content,
            style=lambda: add_dicts(
                style, {"marginLeft": margin(), "marginRight": margin()}
            ),
        )

    return div(
        [
            div(
                a(
                    img(
                        alt="pytek logo",
                        src="website/static/cogs_pytek.svg",
                        style={
                            "height": LOGO_HEIGHT,
                            "marginLeft": "2rem",
                            "marginTop": "1rem",
                        },
                    ),
                    href="#" + HOME_PAGE,
                ),
                style={"height": LOGO_HEIGHT},
            ),
            responsive_margins(
                div(
                    lambda: slides[page_index()],
                    style={
                        "display": "flex",
                        "flexDirection": "column",
                        "justifyContent": "center",
                        "height": "100%",
                    },
                ),
                style={
                    "flex": 1,
                },
            ),
            # dummy bottom div to ensure the main one is centered
            div(None, style={"height": "100px"}),
            div(
                bottom,
                style={
                    "height": "100px",
                    "width": "100%",
                    "position": "absolute",
                    "bottom": 0,
                },
            ),
        ],
        style={
            "display": "flex",
            "flexDirection": "column",
            "height": "100%",
            "justifyContent": "center",
        },
    )
