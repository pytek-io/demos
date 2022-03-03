from reflect_html import *
from reflect_antd import Select, Typography, Divider
Title = Typography.Title
def app():
    return[
 Title("Ant Design 4.0", level=3),
 Title(""{options.length}" Items", level=4),
 Select(mode="multiple", style=dict(width='100%'), placeholder="Please select", defaultValue=['a10', 'c12'], onChange=handleChange, options=options),
 Divider(),
 Title("Ant Design 3.0", level=3),
 iframe(title="Ant Design 3.0 Select demo", src="https://codesandbox.io/embed/solitary-voice-m3vme?fontsize=14&hidenavigation=1&theme=dark&view=preview", style=dict(width='100%', height=300)),
]