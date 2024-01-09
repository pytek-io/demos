from render import create_observable
from render_antd import Popconfirm, Switch, message
from render_html import *


def app():
    raise NotImplementedError("not supported")
#     changeCondition = value => {
#     this.setState({ condition: value });
#   };

#   confirm = () => {
#     this.setState({ visible: false });
#     message.success('Next step.');
#   };

#   cancel = () => {
#     this.setState({ visible: false });
#     message.error('Click on cancel.');
#   };

#   handleVisibleChange = visible => {
#     if (!visible) {
#       this.setState({ visible });
#       return;
#     }
#     // Determining condition before show the popconfirm.
#     print(this.state.condition);
#     if (this.state.condition) {
#       this.confirm(); // next step
#     } else {
#       this.setState({ visible }); // show the popconfirm
#     }
#   };
    return div(
        [
            Popconfirm(
                a("Delete a task", href="#"),
                title="Are you sure delete this task?",
                visible=this.state.visible,
                onVisibleChange=this.handleVisibleChange,
                onConfirm=this.confirm,
                onCancel=this.cancel,
                okText="Yes",
                cancelText="No",
            ),
            br(),
            br(),
            "Whether directly execute：",
            Switch(defaultChecked=True, onChange=this.changeCondition),
        ]
    )

