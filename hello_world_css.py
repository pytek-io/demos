import render_html as html

CSS = ["demos/hello_world.css"]


def app():
    return html.h1("Hello world!", className="title")
