from reflect_html import h1

CSS = ["demos/hello_world.css"]

def app():
    return h1("Hello world!", className="title")