import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def confirm():
    antd.Modal.confirm(
        {
            "title": "Confirm",
            "icon": ant_icons.ExclamationCircleOutlined(),
            "content": "Bla bla ...",
            "okText": "确认",
            "cancelText": "取消",
        }
    )


def app(_):
    visible = r.ObservableValue(False)
    return antd.Space(
        [
            antd.Button("Modal", type="primary", onClick=lambda: visible.set(True)),
            antd.Modal(
                [html.p("Bla bla ..."), html.p("Bla bla ..."), html.p("Bla bla ...")],
                title="Modal",
                open=visible,
                onOk=lambda: visible.set(False),
                onCancel=lambda: visible.set(False),
                okText="确认",
                cancelText="取消",
            ),
            antd.Button("Confirm", onClick=confirm),
        ]
    )
