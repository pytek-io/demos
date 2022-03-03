from reflect_html import *
from reflect_antd import Calendar, Alert
from reflect import make_observable, Callback


def app():
    selected_value = make_observable(None)

    def selected_value_formatted():
        value = selected_value()
        return value.strftime("%Y-%M-%D") if value else "nothing"

    return div(
        [
            Alert(message=lambda: f"You selected {selected_value_formatted()}"),
            Calendar(
                onSelect=Callback(selected_value.set),
            ),
        ]
    )
