import render_antd as antd
import render_html as html


def app(_):
    reverse_switch = antd.Switch(size="small")
    return html.div(
        [
            antd.Slider(defaultValue=30, reverse=reverse_switch),
            antd.Slider(range=True, defaultValue=[20, 50], reverse=reverse_switch),
            "Reversed: ",
            reverse_switch,
        ]
    )
