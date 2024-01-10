import render_antd as antd


def app(_):
    return antd.Badge.Ribbon(
        antd.Card("And raises the spyglass."), text="Pushes open the window"
    )
