import render_antd as antd
import render_html as html


def app(_):
    return antd.Descriptions(
        [
            antd.Descriptions.Item("Zhou Maomao", label="UserName"),
            antd.Descriptions.Item("1810000000", label="Telephone"),
            antd.Descriptions.Item("Hangzhou, Zhejiang", label="Live"),
            antd.Descriptions.Item(
                "No. 18, Wantang Road, Xihu District, Hangzhou, Zhejiang, China",
                label="Address",
                span=2,
            ),
            antd.Descriptions.Item("empty", label="Remark"),
        ],
        title="User Info",
        layout="vertical",
    )
