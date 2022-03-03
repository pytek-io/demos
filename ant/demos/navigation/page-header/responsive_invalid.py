from reflect_html import *
from reflect_antd import PageHeader, Tabs, Button, Statistic, Descriptions
TabPane = Tabs.TabPane
renderContent = Descriptions([Descriptions.Item("Lili Qu", label="Created"), Descriptions.Item(a("421421"), label="Association"), Descriptions.Item("2017-01-10", label="Creation Time"), Descriptions.Item("2017-10-10", label="Effective Time"), Descriptions.Item("Gonghu Road, Xihu District, Hangzhou, Zhejiang, China", label="Remarks")], size="small", column=column)
extraContent = div([Statistic(title="Status", value="Pending", style=dict(marginRight=32)), Statistic(title="Price", prefix="$", value=568.08)], style=dict(display='flex', width='max-content', justifyContent='flex-end'))
Content = div([div(""{children}"", className="main"), div(""{extra}"", className="extra")], className="content")
def app():
    return[
 PageHeader("Operation", className="site-page-header-responsive", onBack=lambda :window.history.back(), title="Title", subTitle="This is a subtitle", extra="{[         <Button key=", 3"=True),
 Button("Operation", key="2"),
 Button("Primary", key="1", type="primary"),
 Tabs([TabPane(tab="Details", key="1"), TabPane(tab="Rule", key="2")], defaultActiveKey="1"),
 Content(""{renderContent()}"", extra=extraContent),
]