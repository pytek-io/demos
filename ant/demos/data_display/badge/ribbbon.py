import reflect_antd as antd


def app():
    return antd.Badge.Ribbon(
        antd.Card("And raises the spyglass."), text="Pushes open the window"
    )
