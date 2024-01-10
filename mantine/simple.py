"""Formula as a lambda expression"""
import render_mantine as mantine


def app(_):
    name = mantine.TextInput(defaultValue="John")
    greeting = lambda: f"Hello {name()}"
    greeting_component = mantine.Text(greeting)
    return mantine.Group([name, greeting_component])
