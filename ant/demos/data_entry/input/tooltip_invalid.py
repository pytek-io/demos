from render_html import *
from render_antd import Input, Tooltip
from render import js
from render import create_observable

value = e.value
value, onBlur, onChange = this.value, this.onBlur, this.onChange
value = this.value


def format_number(value):
    pass


def app():
    value = create_observable(0)

    def result():
        if actual_value := value():
            formatted_value = (
                formatNumber(actual_value) if actual_value != "-" else actual_value
            )
            title = span(formatted_value, className="numeric-input-title")
        else:
            title = "Input a number"
        return Tooltip(
            Input(
                # "{...this.props}"=True,
                onChange=this.onChange,
                onBlur=this.onBlur,
                placeholder="Input a number",
                maxLength=25,
            ),
            trigger=["focus"],
            title=title,
            placement="topLeft",
            overlayClassName="numeric-input",
        )


def app():
    return NumericInput(
        style=dict(width=120), value=this.state.value, onChange=this.onChange
    )
