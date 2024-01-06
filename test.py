import render_html as html


def app():
    return html.div(
        [html.h1("Hello, World!"), html.p("This is a test of the render_html module.")]
    )
