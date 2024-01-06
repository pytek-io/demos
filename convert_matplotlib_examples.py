import ast
import os

import astunparse
import black


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
        return black.format_str(code, mode=black.FileMode())
    except:
        print(code)
        raise


def generate_demo(module_content, origin):
    lines = [line for line in module_content.split("\n") if "plt.show()" not in line]
    module = ast.parse("\n".join(lines))
    description = (
        module.body[0].value.s + f"\nThis example has been taken from {origin}."
    )
    last_method_index = len(module.body) - next(
        (
            index
            for index, element in enumerate(reversed(module.body))
            if isinstance(element, ast.FunctionDef)
        ),
        len(module.body) - 1,
    )
    app_body, body = [], module.body[1:last_method_index]
    for element in module.body[last_method_index:]:
        if isinstance(element, ast.If) and all(
            x in astunparse.unparse(element.test)
            for x in ["__name__", "==", "__main__"]
        ):
            app_body.extend(element.body)
        else:
            m = (
                body
                if isinstance(
                    element, (ast.FunctionDef, ast.Import, ast.ImportFrom, ast.ClassDef)
                )
                else app_body
            )
            m.append(element)
    app = ast.parse(app_template).body[0]
    app.body = app_body + app.body
    body.append(app)
    module.body = body
    return preamble(f'"""{description}\n"""') + astunparse.unparse(module)


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
        result += content[previous:]
    else:
        result = content
    return result


SKIP_FOLDERS = [
    "user_interfaces",
    "userdemo",
    "widgets",
    "event_handling",
    "units",
    "animation",
]
DESTINATION_FOLDER = "matplotlib_examples"
SOURCE_FOLDER = "../matplotlib/examples"
import importlib
import shutil


def purge_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)


import render.common as r
import render.controller as r


def main():
    r.CURRENT_CONTROLLER.set(r.DefaultController())
    purge_folder(DESTINATION_FOLDER)
    i = 0
    for path, _dirs, files in os.walk(SOURCE_FOLDER):
        if os.path.split(path)[-1] in SKIP_FOLDERS:
            continue
        for filename in files:
            if filename.endswith(".py"):
                i += 1
                dest = os.path.join(*((DESTINATION_FOLDER,) + os.path.split(path)[1:]))
                if not os.path.exists(dest):
                    os.makedirs(dest)
                print(i, os.path.join(path[3:], filename))
                content = open(os.path.join(path, filename)).read()
                origin = f"https://github.com/matplotlib/matplotlib/blob/main/{os.path.join(path[3:], filename)}"
                new_content = unprotect(generate_demo(protect(content), origin))
                file_path = os.path.join(dest, filename)
                open(file_path, "w").write(black(new_content))
                try:
                    importlib.import_module(
                        os.path.join(dest, filename).replace(os.sep, ".")[:-3]
                    ).app()
                except:
                    os.remove(file_path)


main()
