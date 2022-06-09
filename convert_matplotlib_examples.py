from ast import ClassDef, parse, FunctionDef, Import, ImportFrom, If
from astunparse import unparse
import os
from os.path import join, split, exists
from black import FileMode, format_str


def preamble(origin):
    return f"""
'''
This example has been adapted from {origin}
'''

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


def generate_demo(module_content, origin):
    module = parse(module_content)
    app_body, body = [], []
    for element in module.body[1:]:
        if (isinstance(element, FunctionDef) and element.name == "demo") or (
            isinstance(element, If)
            and all(x in unparse(element.test) for x in ["__name__", "==", "__main__"])
        ):
            app_body.extend(element.body)
            break  # assuming tha we are only calling demo afterward...
        else:
            m = (
                body
                if isinstance(element, (FunctionDef, Import, ImportFrom, ClassDef))
                else app_body
            )
            m.append(element)
    app = parse(app_template).body[0]
    app.body = app_body[:-2] + app.body
    body.append(app)
    module.body = body
    return preamble(origin) + unparse(module)


def main():
    i = 0
    for path, _dirs, files in os.walk("../examples"):
        for filename in files:
            if filename.endswith(".py"):
                i+=1
                dest = join(*(("../matplotlib_examples",) + split(path)[1:]))
                if not exists(dest):
                    os.makedirs(dest)
                print(join(path[3:], filename))
                open(join(dest, filename), "w").write(
                    black(
                        generate_demo(
                            open(join(path, filename)).read(),
                            f"https://github.com/matplotlib/matplotlib/blob/main/{join(path[3:], filename)}",
                        )
                    )
                )
    print(i)

main()

# print(
#     generate_demo(
#         open("../examples/axes_grid1/demo_axes_hbox_divider.py").read(), "whatever"
#     )
# )
