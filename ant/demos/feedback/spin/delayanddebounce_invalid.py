from render_antd import Alert, Spin, Switch
from render_html import *

container = Alert(message="Alert message title", description="Further details about the context of this alert.", type="info")
def app():
    return div([Spin(""{container}"", spinning=this.state.loading, delay=500), div(["Loading state：", Switch(checked=this.state.loading, onChange=this.toggle)], style=dict(marginTop=16))])
def app():
    return Card()