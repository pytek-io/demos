from ast import ClassDef, parse, FunctionDef, Import, ImportFrom, If
from astunparse import unparse
import os
from os.path import join, split, exists
from black import FileMode, format_str


def preamble(description):
    return f"""
{description}

import matplotlib
matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock 
from demos.charts.utils import matplotlib_to_svg
"""


app_template = """def app():
    return matplotlib_to_svg(fig)"""


def black(code):
    try:
        return format_str(code, mode=FileMode())
    except:
        # return code
        print(code)
        raise


# matplotlib_examples.images_contours_and_fields.plot_streamplot
# matplotlib_examples.lines_bars_and_markers.marker_reference
# matplotlib_examples.lines_bars_and_markers.multivariate_marker_plot
# matplotlib_examples.misc.custom_projection
# matplotlib_examples.misc.demo_agg_filter
# matplotlib_examples.misc.demo_ribbon_box


def generate_demo(module_content, origin):
    lines = [line for line in module_content.split("\n") if "plt.show()" not in line]
    module = parse("\n".join(lines))
    description = (
        module.body[0].value.s + f"\nThis example has been taken from {origin}."
    )
    last_method_index = len(module.body) - next(
        (
            index
            for index, element in enumerate(reversed(module.body))
            if isinstance(element, FunctionDef)
        ),
        len(module.body) - 1,
    )
    app_body, body = [], module.body[1:last_method_index]
    for element in module.body[last_method_index:]:
        if isinstance(element, If) and all(
            x in unparse(element.test) for x in ["__name__", "==", "__main__"]
        ):
            app_body.extend(element.body)
        else:
            m = (
                body
                if isinstance(element, (FunctionDef, Import, ImportFrom, ClassDef))
                else app_body
            )
            m.append(element)
    app = parse(app_template).body[0]
    app.body = app_body + app.body
    body.append(app)
    module.body = body
    return preamble(f'"""{description}\n"""') + unparse(module)


def match_delimiters(content: str, delimiter: str):
    index = 0
    while delimiter in content[index:]:
        start = content.index(delimiter, index)
        end = content.index(delimiter, start + len(delimiter))
        index = end + len(delimiter)
        yield start + len(delimiter), end


def protect(content: str):
    delimiter = '"""' if '"""' in content else "'''"
    indexes = list(match_delimiters(content, delimiter))[1:]
    if indexes:
        result, previous = "", 0
        for start, end in indexes:
            result += content[previous:start] + "&&&" + content[start:end] + "&&&"
            previous = end
        result += content[previous:]
    else:
        result = content
    return result


def unprotect(content: str):
    indexes = list(match_delimiters(content, "&&&"))
    if indexes:
        result, previous = "", 0
        for start, end in indexes:
            prev = content[previous : start - 4]
            comment = content[start:end].replace("\\n", "\n")
            result += prev + "'''" + comment + "'''"
            previous = end + 4
        result += content[previous :]
    else:
        result = content
    return result

SKIP_FOLDERS = ["user_interfaces", "userdemo", "widgets", "event_handling", "units", "animation"]
DESTINATION_FOLDER = "matplotlib_examples"
SOURCE_FOLDER = "../matplotlib/examples"
import shutil
import importlib

def purge_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)

from reflect.common import CURRENT_CONTROLLER
from reflect.controller import DefaultController

def main():
    CURRENT_CONTROLLER.set(DefaultController())
    purge_folder(DESTINATION_FOLDER)
    i = 0
    for path, _dirs, files in os.walk(SOURCE_FOLDER):
        if os.path.split(path)[-1] in SKIP_FOLDERS:
            continue
        for filename in files:
            if filename.endswith(".py"):
                i += 1
                dest = join(*((DESTINATION_FOLDER,) + split(path)[1:]))
                if not exists(dest):
                    os.makedirs(dest)
                print(i, join(path[3:], filename))
                content = open(join(path, filename)).read()
                origin = f"https://github.com/matplotlib/matplotlib/blob/main/{join(path[3:], filename)}"
                new_content = unprotect(generate_demo(protect(content), origin))
                file_path = join(dest, filename)
                open(file_path, "w").write(black(new_content))
                try:
                    importlib.import_module(join(dest, filename).replace(os.sep, ".")[:-3]).app()
                except:
                    os.remove(file_path)
main()

