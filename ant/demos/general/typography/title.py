from reflect_html import *
from reflect_antd import Typography

Title = Typography.Title


def app():
    return [
        Title("h1. Ant Design"),
        Title("h2. Ant Design", level=2),
        Title("h3. Ant Design", level=3),
        Title("h4. Ant Design", level=4),
        Title("h5. Ant Design", level=5),
    ]
