import os
import pickle
import re

import mistletoe
import reflect_antd as antd
import reflect_html as html
import reflect_monaco as monaco
import reflect_utils
import yaml
import pathlib
import reflect as r


def is_header_two(token):
    return isinstance(token, mistletoe.block_token.Heading) and token.level == 2


def split_list(elements, size):
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
MAIN_COL_BREAK_POINTS = dict(xs=24, sm=24, md=18, lg=18, xl=19, xxl=20)
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
DISPLAY_DEMOS_ERRORS = True


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
    return monaco.Editor(
        defaultValue="\n".join(content),
        options=options,
        defaultLanguage=language,
        height=height,
    )


def build_menu(root_directory):
    root_directory = root_directory + "/demos"
    sub_menus = []
    for category in CATEGORIES:
        category_folder = os.path.join(root_directory, category)
        nice_category_name = pickle.loads(
            open(os.path.join(category_folder, "description.pick"), "rb").read()
        )
        menuItems = []
        for component_name in sorted(os.listdir(category_folder)):
            component_folder = pathlib.Path(category_folder, component_name)
            if not component_folder.is_dir():
                continue
            nb_cols = int(
                pathlib.Path(component_folder, "summary.txt")
                .read_text()
                .splitlines()[0]
            )
            COMPONENTS_PROPS[component_name] = nb_cols
            menuItems.append(
                {"label": component_name, "key": f"{category}/{component_name}"}
            )
        sub_menus.append(
            {"children": menuItems, "label": nice_category_name, "key": category}
        )
    first_item_key = sub_menus[0]["children"][0]["key"]
    current_method = r.ObservableValue(first_item_key, key="first_item_key")
    return current_method, antd.Menu(
        items=sub_menus,
        mode="inline",
        defaultSelectedKeys=[first_item_key],
        defaultOpenKeys=[sub_menus[0]["key"]],
        onClick=r.Callback(current_method.set, args="key"),
    )


def format_md_text(md_text):
    result = []
    previous_end = 0
    for m in re.finditer("`\\w+`", md_text):
        start, end = m.start(), m.end()
        if start > previous_end:
            result.append(md_text[previous_end : m.start()])
        result.append(html.code(md_text[start + 1 : end - 1]))
        previous_end = end
    if previous_end < len(md_text):
        result.append(md_text[previous_end:])
    return html.div(html.p(result))


def code_box_bottom(description, js, py):
    show_code_editor = r.ObservableValue(True, key="show_code_editor")

    def result():
        result, add_code = [], False
        if show_code_editor():
            img_ = html.img(
                alt="collapse code",
                src=COLLAPSE_ICON_PATH,
                className="code-expand-icon-show",
            )
        else:
            img_ = html.img(
                alt="expand code",
                src=EXPAND_ICON_PATH,
                className="code-expand-icon-show",
            )
            add_code = True
        result = [
            html.div(
                [html.span(img_, className="code-expand-icon code-box-code-action")],
                className="code-box-actions",
                onClick=reflect_utils.toggle_observable(show_code_editor),
            )
        ]
        if add_code:
            result.append(
                antd.Tabs(
                    [
                        antd.Tabs.TabPane(
                            create_code_editor(
                                "python", py, height=f"{len(py) * 18}px"
                            ),
                            tab="Python",
                            key="py",
                        ),
                        antd.Tabs.TabPane(
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
                html.div(format_md_text(description), className="code-box-description")
            )
        return html.div(result)

    return result


def create_code_box(
    module_path, component_name, module_name, demo_name, description, js_code
):
    python_module_path = reflect_utils.get_module_name(module_path)
    success, _css, _title, demo = reflect_utils.evaluate_demo_module(python_module_path)
    if not success and not DISPLAY_DEMOS_ERRORS:
        return None
    return html.section(
        [
            html.div(
                [
                    demo_name,
                    html.span(
                        reflect_utils.create_edit_link(
                            module_path, __file__, css=["/demos/ant_demo_extra.css"]
                        ),
                        className="anticon anticon-edit",
                    ),
                ],
                className="code-box-title",
            ),
            html.section(demo, className="code-box-demo"),
            code_box_bottom(description, js_code, open(module_path).read().split("\n")),
        ],
        id=f"components-{component_name}-demo-{module_name}",
        className="code-box",
        style={} if success else dict(borderColor="red", borderStyle="solid"),
    )


def demo_details(root_directory, category, component_name):
    default_folder = os.path.join(root_directory, "demos", category, component_name)
    _nb_cols, demos = (
        pathlib.Path(default_folder, "summary.txt").read_text().split("\n")
    )
    for module_name, demo_name in (x.split(":") for x in demos.split(",")):
        module_path = pathlib.Path(default_folder, module_name + ".py")
        if not module_path.exists():
            continue
        maybe_code_box = create_code_box(
            str(module_path.relative_to(os.getcwd())),
            component_name,
            module_name,
            demo_name,
            pathlib.Path(default_folder, module_name + ".md").read_text(),
            pathlib.Path(default_folder, module_name + ".jsx").read_text(),
        )
        if maybe_code_box:
            yield maybe_code_box


def generate_top_level_components(source, demos):
    yielded_demos = False
    for token in mistletoe.Document(
        reflect_utils.replace_weird_escaped_pipes(source)
    ).children:
        if isinstance(token, mistletoe.block_token.SetextHeading):
            definitions = "\n".join(
                row.content
                for row in token.children
                if not isinstance(row, mistletoe.span_token.LineBreak)
            )
            yield html.h1(yaml.safe_load(definitions)["title"])
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
                html.h2("Examples"),
                antd.Row(demos),
                reflect_utils.render_node(token),
            ]
            yielded_demos = True
        else:
            component = reflect_utils.render_node(token)
            if component:
                yield component


def app():
    root_directory, _ = os.path.split(__file__)
    current_demo_path, menu = build_menu(root_directory)

    def page_display():
        category, component_name = current_demo_path().split("/")
        demos = list(demo_details(root_directory, category, component_name))
        if COMPONENTS_PROPS[component_name] == 1:
            demos = antd.Col(demos)
        else:
            demos = [
                antd.Col(
                    elements, span=12, style=dict(paddingLeft="8px", paddingRight="8px")
                )
                for elements in split_list(demos, 2)
            ]
        s = open(f"demos/ant/definitions/{component_name}.md").read()
        styles, content = reflect_utils.extract_style_definitions(s)
        md_description = list(generate_top_level_components(content, demos))
        return html.section(
            antd.Row(
                antd.Col(md_description + ([html.style(styles)] if styles else [])),
                style=dict(marginLeft="-8px", marginRight="-8px", rowGap="0px"),
            ),
            className="markdown",
        )

    menu_col = antd.Col([], **MENU_COL_BREAK_POINTS)
    main_col = antd.Col(
        html.h1("Ant components explorer", style=dict(paddingLeft=200, paddingTop=10)),
        **MAIN_COL_BREAK_POINTS,
    )
    row = antd.Row(
        [menu_col, main_col],
        style={"rowGap": "0px", "flexFlow": "row nowrap", "height": "64px"},
    )
    return html.div(
        [
            html.header(row, id="header", className="clearfix"),
            html.div(
                antd.Row(
                    [
                        antd.Col(menu, **MENU_COL_BREAK_POINTS),
                        antd.Col(
                            [
                                html.section(
                                    html.article(page_display),
                                    className="main-container main-container-component",
                                )
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
