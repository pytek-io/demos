import os
import pickle
import re
from os.path import join, split

import yaml
from mistletoe import Document, block_token, span_token
from reflect import Callback, create_observable
from reflect_antd import Col, Menu, Row, Tabs
from reflect_html import (
    article,
    code,
    div,
    h1,
    h2,
    header,
    img,
    p,
    section,
    span,
    style,
)
from reflect_monaco import Editor as CodeEditor
from reflect_utils.common import (
    create_edit_link,
    evaluate_demo_module,
    toggle_observable,
)
from reflect_utils.md_parsing import (
    extract_style_definitions,
    render_node,
    replace_weird_escaped_pipes,
)
from reflect_utils.misc import get_module_name


def is_header_two(token):
    return isinstance(token, block_token.Heading) and token.level == 2

def split_list(elements, size):
    # should simply be zip(*chunk(elements, size)), but for some reasons
    # this does not work with components and size 2 (super weird...)
    result = [[] for i in range(size)]
    for i, element in enumerate(elements):
        result[i % size].append(element)
    return result


CATEGORIES = [
    "general",
    "layout",
    "navigation",
    "data_entry",
    "data_display",
    "feedback",
    "other",
]
MENU_COL_BREAK_POINTS = dict(xs=24, sm=24, md=6, lg=6, xl=5, xxl=4)
MAIN_COL_BREAK_POINTS = dict(
    xs=24,
    sm=24,
    md=18,
    lg=18,
    xl=19,
    xxl=20,
)

ANT_LOGO_ICON_PATH = "website/static/ant_logo.svg"

COLLAPSE_ICON_PATH = "website/static/collapse_icon.svg"
EXPAND_ICON_PATH = "website/static/expand_icon.svg"

COMPONENTS_PROPS = {}
TITLE = "Ant Components"
CSS = [
    "website/ant_site_index.css",
    "demos/ant_markdown.css",
    "demos/ant_site_logo.css",
    "demos/ant/collated.css",
]
JS_MODULES = ["ant_demo"]
FAVICON = ANT_LOGO_ICON_PATH

DISPLAY_DEMOS_ERRORS = False


def create_code_editor(
    language, content, relaxed=False, height=None, lineNumbers=False, readOnly=True
):
    options = dict(
        minimap={"enabled": False},
        lineNumbers=lineNumbers,
        glyphMargin=False,
        wordWrap=True,
        renderValidationDecorations="off" if relaxed else "on",
        readOnly=readOnly,
    )
    return CodeEditor(
        defaultValue="\n".join(content),
        options=options,
        defaultLanguage=language,
        height=height,
    )


def build_menu(rootdir):
    rootdir = rootdir + "/demos"
    sub_menus = []
    for category in CATEGORIES:
        category_folder = join(rootdir, category)
        nice_category_name = pickle.loads(
            open(join(category_folder, "description.pick"), "rb").read()
        )
        menuItems = []
        for component_name in sorted(os.listdir(category_folder)):
            component_folder = join(category_folder, component_name)
            if not os.path.isdir(component_folder):
                continue
            summary_path = join(component_folder, "summary.pick")
            if not os.path.exists(summary_path):
                print("skipping", component_name, "no summary found")
                continue
            nice_component_name, nb_cols = pickle.loads(
                open(summary_path, "rb").read()
            )[:2]
            COMPONENTS_PROPS[component_name] = nb_cols
            menuItems.append(
                Menu.Item(
                    nice_component_name,
                    key=f"{category}/{component_name}",
                )
            )
        sub_menus.append(
            Menu.SubMenu(menuItems, title=nice_category_name, key=category)
        )
    first_item_key = sub_menus[0].children[0]._key
    current_method = create_observable(first_item_key, key="first_item_key")
    return current_method, Menu(
        sub_menus,
        mode="inline",
        defaultSelectedKeys=[first_item_key],
        defaultOpenKeys=[sub_menus[0]._key],
        onClick=Callback(current_method.set, args="key"),
    )


def format_md_text(md_text):
    result = []
    previous_end = 0
    for m in re.finditer("`\w+`", md_text):
        start, end = m.start(), m.end()
        if start > previous_end:
            result.append(md_text[previous_end : m.start()])
        result.append(code(md_text[start + 1 : end - 1]))
        previous_end = end
    if previous_end < len(md_text):
        result.append(md_text[previous_end:])
    return div(p(result))


def code_box_bottom(description, js, py):
    show_code_editor = create_observable(True, key="show_code_editor")

    def result():
        result, add_code = [], False
        if show_code_editor():
            img_ = img(
                alt="collapse code",
                src=COLLAPSE_ICON_PATH,
                className="code-expand-icon-show",
            )
        else:
            img_ = img(
                alt="expand code",
                src=EXPAND_ICON_PATH,
                className="code-expand-icon-show",
            )
            add_code = True
        result = [
            div(
                [
                    span(
                        img_,
                        className="code-expand-icon code-box-code-action",
                    ),
                ],
                className="code-box-actions",
                onClick=toggle_observable(show_code_editor),
            )
        ]
        if add_code:
            result.append(
                Tabs(
                    [
                        Tabs.TabPane(
                            create_code_editor(
                                "python", py, height=f"{len(py) * 18}px"
                            ),
                            tab="Python",
                            key="py",
                        ),
                        Tabs.TabPane(
                            create_code_editor(
                                "typescript", js, True, height=f"{len(js) * 18}px"
                            ),
                            tab="JS",
                            key="js",
                        ),
                    ],
                    centered=True,
                )
            )
        if description:
            result.append(
                div(format_md_text(description), className="code-box-description")
            )
        return div(result)

    return result


def create_code_box(
    module_path,
    component_name,
    module_name,
    demo_name,
    description,
    js_code,
):
    python_module_path = get_module_name(module_path)
    success, _css, _title, demo = evaluate_demo_module(python_module_path)
    if not success and not DISPLAY_DEMOS_ERRORS:
        return None
    return section(
        [
            div(
                [
                    demo_name,
                    span(
                        create_edit_link(
                            module_path, __file__, css=["/demos/ant_demo_extra.css"]
                        ),
                        className="anticon anticon-edit",
                    ),
                ],
                className="code-box-title",
            ),
            section(demo, className="code-box-demo"),
            code_box_bottom(description, js_code, open(module_path).read().split("\n")),
        ],
        id=f"components-{component_name}-demo-{module_name}",
        className="code-box",
        style={} if success else dict(borderColor="red", borderStyle="solid"),
    )


def demo_details(rootdir, category, component_name):
    default_folder = join(rootdir, "demos", category, component_name)
    _nice_name, _nb_cols, demos = pickle.loads(
        open(os.path.join(default_folder, "summary.pick"), "rb").read()
    )
    for _order, module_name, js, description, demo_name in sorted(
        demos, key=lambda x: x[0]
    ):
        module_path = os.path.join(default_folder, module_name + ".py")
        if not os.path.exists(module_path):
            continue
        module_path = module_path[len(os.getcwd()):]
        maybe_code_box = create_code_box(
            module_path[1:] if module_path.startswith(os.path.sep) else module_path,
            component_name,
            module_name,
            demo_name,
            description,
            js,
        )
        if maybe_code_box:
            yield maybe_code_box


def generate_top_level_components(source, demos):
    yielded_demos = False
    for token in Document(replace_weird_escaped_pipes(source)).children:
        if isinstance(token, block_token.SetextHeading):
            definitions = "\n".join(
                row.content
                for row in token.children
                if not isinstance(row, span_token.LineBreak)
            )
            yield h1(yaml.safe_load(definitions)["title"])
        elif (
            is_header_two(token)
            and token.children[0].content
            not in [
                "When To Use",
                "Specification",
                "Component Overview",
                "Visualization rules",
            ]
            and not yielded_demos
        ):
            yield from [
                h2("Examples"),
                Row(demos),
                render_node(token),
            ]
            yielded_demos = True
        else:
            component = render_node(token)
            if component:
                yield component


def app():
    rootdir, _ = split(__file__)
    current_demo_path, menu = build_menu(rootdir)

    def page_display():
        category, component_name = current_demo_path().split("/")
        demos = list(demo_details(rootdir, category, component_name))
        if COMPONENTS_PROPS[component_name] == 1:
            demos = Col(demos)
        else:
            demos = [
                Col(
                    elements,
                    span=12,
                    style=dict(paddingLeft="8px", paddingRight="8px"),
                )
                for elements in split_list(demos, 2)
            ]
        s = open(f"demos/ant/definitions/{component_name}.md").read()
        styles, content = extract_style_definitions(s)
        md_description = list(generate_top_level_components(content, demos))
        return section(
            Row(
                Col(md_description + ([style(styles)] if styles else [])),
                style=dict(marginLeft="-8px", marginRight="-8px", rowGap="0px"),
            ),
            className="markdown",
        )
    menu_col = Col(
        [], **MENU_COL_BREAK_POINTS
    )
    main_col = Col(
        h1("Ant components explorer", style=dict(paddingLeft=200, paddingTop=10)),
        **MAIN_COL_BREAK_POINTS,
    )
    row = Row(
        [menu_col, main_col],
        style={"rowGap": "0px", "flexFlow": "row nowrap", "height": "64px"},
    )
    return div(
        [
            header(row, id="header", className="clearfix"),
            div(
                Row(
                    [
                        Col(menu, **MENU_COL_BREAK_POINTS),
                        Col(
                            [
                                section(
                                    article(page_display),
                                    className="main-container main-container-component",
                                ),
                            ],
                            **MAIN_COL_BREAK_POINTS,
                        ),
                    ],
                    gutter={"xs": 8, "sm": 16, "md": 24, "lg": 32},
                ),
                className="main-wrapper",
            ),
        ]
    )
