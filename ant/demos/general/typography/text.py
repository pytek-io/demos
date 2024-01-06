import render_antd as antd
import render_html as html

Text, Link = antd.Typography.Text, antd.Typography.Link


def app():
    return antd.Space(
        [
            Text("Ant Design (default)"),
            Text("Ant Design (secondary)", type="secondary"),
            Text("Ant Design (success)", type="success"),
            Text("Ant Design (warning)", type="warning"),
            Text("Ant Design (danger)", type="danger"),
            Text("Ant Design (disabled)", disabled=True),
            Text("Ant Design (mark)", mark=True),
            Text("Ant Design (code)", code=True),
            Text("Ant Design (keyboard)", keyboard=True),
            Text("Ant Design (underline)", underline=True),
            Text("Ant Design (delete)", delete=True),
            Text("Ant Design (strong)", strong=True),
            Link("Ant Design (Link)", href="https://ant.design", target="_blank"),
        ],
        direction="vertical",
    )
