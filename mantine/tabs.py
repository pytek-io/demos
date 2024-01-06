"""Formula as a lambda expression"""
import render_mantine as mantine
import render_tabler_icons as tabler_icons

def app():
    name = mantine.Tabs(
        mantine.Tabs.List()
    )
    greeting = lambda: f"Hello {name()}"
    greeting_component = mantine.Text(greeting)
    return mantine.Group([name, greeting_component])

