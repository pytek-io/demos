import render as r
import render_antd as antd
import render_html as html

default_options = ["Daily", "Weekly", "Monthly"]


def app():
    options = r.ObservableList(default_options.copy())

    def handle_click():
        if len(options) == len(default_options):
            options.extend(["Quarterly", "Yearly"])

    return html.div(
        [
            antd.Segmented(defaultValue=default_options[0], options=options),
            html.br(),
            antd.Button("Add more options", onClick=handle_click),
        ]
    )
