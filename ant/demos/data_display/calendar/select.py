import render as r
import render_antd as antd
import render_html as html


def app():
    selected_value = r.ObservableValue()

    def selected_value_formatted():
        value = selected_value()
        return value.strftime("%Y-%M-%d") if value else "nothing"

    return html.div(
        [
            antd.Alert(message=lambda: f"You selected {selected_value_formatted()}"),
            antd.Calendar(onSelect=selected_value.set),
        ]
    )
