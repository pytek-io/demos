from reflect_html import *
from reflect_antd import Spin, Alert, Switch
container = Alert(message="Alert message title", description="Further details about the context of this alert.", type="info")
def app():
    return div([Spin(""{container}"", spinning=this.state.loading, delay=500), div(["Loading state：", Switch(checked=this.state.loading, onChange=this.toggle)], style=dict(marginTop=16))])
def app():
    return Card()