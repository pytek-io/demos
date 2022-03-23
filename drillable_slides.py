import itertools
import os
from functools import partial

import yaml
from reflect import ResponsiveValue, get_window, make_observable, CachedEvaluation
from reflect_html import a, div, img, path, svg
from reflect_swiper import Swiper, SwiperSlide
from website.common import BACKGROUND_COLOR, FONT_FAMILY, GREEN, LIGHT_BLUE
from website.home import SLOGAN
from website.main import HTML_LINKS
from website.reflect.gallery import MENU as GALLERY_MENU

TITLE = "Early adopters presentation"
BODY_STYLE = {"backgroundColor": "rgb" + str(BACKGROUND_COLOR), "fontSize": 10}
CSS = ["test.css"]
RIGHT_ARROW = 39
LEFT_ARROW = 37
LOGO_HEIGHT = 52
BOTTOM_HEIGHT = 52
HOME_PAGE = "website.home"


maximize = "M396.795 396.8H320V448h128V320h-51.205zM396.8 115.205V192H448V64H320v51.205zM115.205 115.2H192V64H64v128h51.205zM115.2 396.795V320H64v128h128v-51.205z"
minimize = "M64 371.2h76.795V448H192V320H64v51.2zm76.795-230.4H64V192h128V64h-51.205v76.8zM320 448h51.2v-76.8H448V320H320v128zm51.2-307.2V64H320v128h128v-51.2h-76.8z"


def select_file_extension(file_path):
    for extension in ["gif", "png", "svg", "jpg"]:
        maybe_path = f"{file_path}.{extension}"
        if os.path.exists(maybe_path):
            return maybe_path


def title(content, color=LIGHT_BLUE, fontSize="2rem"):
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


def create_answer_box(answer, details, detail_level):
    update_detail_level = lambda: detail_level.set(1 if detail_level() == 2 else 2)
    return div(
        div(
            [
                div(
                    lambda: answer + ("" if detail_level() == 2 else ".."),
                    onClick=update_detail_level,
                ),
                lambda: div(
                    details,
                    onClick=update_detail_level,
                )
                if detail_level() == 2
                else None,
            ]
        ),
        style={
            "marginRight": "10px",
            "marginBottom": "20px",
            "fontSize": "1.5rem",
            "color": LIGHT_BLUE,
            "borderColor": GREEN,
            "borderStyle": "dashed",
            "padding": 10,
            "display": "inline-block",
            "pointerEvents": "all",
            "cursor": "pointer",
            "textAlign": "justify",
        },
    )


def create_question_and_answer(
    default_detail_level_value, on_drill_down, question, answer, details
):
    detail_level = make_observable(default_detail_level_value)

    def drill():
        on_drill_down(detail_level)
        detail_level.set(
            default_detail_level_value
            + (0 if detail_level() != default_detail_level_value else 1)
        )

    return div(
        [
            div(
                question,
                onClick=drill,
                style={
                    "fontFamily": FONT_FAMILY,
                    "color": GREEN,
                    "fontSize": "2rem",
                    "padding": 10,
                    "pointerEvents": "all",
                    "cursor": "pointer",
                },
            ),
            lambda: create_answer_box(answer, details, detail_level)
            if detail_level() > 0
            else None,
        ]
    )


def create_page(items, default_detail_level_value):
    current_detail_level = None

    def on_drill_down(new_detail_level):
        nonlocal current_detail_level
        if (
            current_detail_level is not None
            and current_detail_level is not new_detail_level
        ):
            current_detail_level.set(default_detail_level_value)
        current_detail_level = new_detail_level

    return div(
        [
            create_question_and_answer(default_detail_level_value, on_drill_down, *item)
            for item in items
        ],
        style={
            # "maxHeight": f"calc(100vh - {BOTTOM_HEIGHT + LOGO_HEIGHT}px)",
            # "overflowY": "scroll",
            "paddingTop": 10
        },
    )


def app():
    window = get_window()
    print(window.hash())
    file_name = window.hash().split("/")[0]
    content = yaml.safe_load(
        open(f"demos/presentations/{file_name}.yaml", "r").read()
    )
    full_screen = make_observable(False)
    details_level = make_observable(0)
    resolution = window.width() * window.height() / 1000
    values = (5, 3, 2)
    if resolution < 300.0:
        values = (3, 2, 1)
    elif resolution > 800:
        window.update_tag_style([("font-size", "24px")], "html")

    NB_QUESTIONS_PER_PAGE = dict(enumerate(values))

    def page_index():
        args = window.hash().split("/")
        return min(int(args[1]) if len(args) > 1 else 0, len(slides()) - 1)

    def set_page_index(index):
        window.hash.set(f"{file_name}/{index}")

    def safe_increment(increment):
        nonlocal page_index, set_page_index
        page_index_value = page_index()
        if increment:
            if page_index_value + 1 < len(slides()):
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
                fontSize="1.5rem",
            ),
        ],
    )

    def generate_slides():
        details_level_value = details_level()
        return [main_page] + [
            create_page(items, details_level_value)
            for items in grouper(NB_QUESTIONS_PER_PAGE[details_level_value], content)
        ]

    slides = CachedEvaluation(generate_slides)

    full_screen_icon = create_icon(
        lambda: minimize if full_screen() else maximize,
        fill="white",
        width="2.5vh",
        height="2.5vh",
        style={
            "pointerEvents": "all",
            "cursor": "pointer",
        },
        onClick=lambda: window.update_full_screen(not full_screen()),
    )

    detail_level_icon = img(
        src=lambda: f"reflect/static/menu-icon-{details_level() + 1}.svg",
        style=dict(width="1.6vh", pointerEvents="all", cursor="pointer"),
        onClick=lambda: details_level.set((details_level() + 1) % 3),
    )

    def page_bullets():
        page_index_value = page_index()
        return [
            create_bullet(
                transparent=page_index_value != index,
                color="white",
                onClick=partial(set_page_index, index),
            )
            for index in range(len(slides()))
        ]

    bottom = div(
        left_center_right(full_screen_icon, detail_level_icon, page_bullets),
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
            xs=10, sm="10vh", md="10vh", lg=None, xl=None, xxl="30vh"
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
                    href="https://pytek.io",
                    target="_blank",
                ),
                style={"height": LOGO_HEIGHT},
            ),
            responsive_margins(
                div(
                    lambda: slides()[page_index()],
                    style={
                        "display": "flex",
                        "flexDirection": "column",
                        "justifyContent": "center",
                        "height": "100%",
                    },
                ),
                style={"flex": 1},
            ),
            # dummy bottom div to ensure the main one is centered
            div(None, style={"height": BOTTOM_HEIGHT}),
            div(
                bottom,
                style={
                    "height": BOTTOM_HEIGHT,
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
