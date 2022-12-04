import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Descriptions(
        [
            antd.Descriptions.Item("Zhou Maomao", label="UserName"),
            antd.Descriptions.Item("1810000000", label="Telephone"),
            antd.Descriptions.Item("Hangzhou, Zhejiang", label="Live"),
            antd.Descriptions.Item("empty", label="Remark"),
            antd.Descriptions.Item(
                "No. 18, Wantang Road, Xihu District, Hangzhou, Zhejiang, China",
                label="Address",
            ),
        ],
        title="User Info",
    )
