from reflect_html import *
from reflect_antd import PageHeader, Tag, Button, Statistic, Descriptions, Row
def app():
    return[
 PageHeader("Operation", className="site-page-header", onBack=lambda :window.history.back(), title="Title", subTitle="This is a subtitle", extra="{[         <Button key=", 3"=True),
 Button("Operation", key="2"),
 Button("Primary", key="1", type="primary"),
 Descriptions([Descriptions.Item("Lili Qu", label="Created"), Descriptions.Item(a("421421"), label="Association"), Descriptions.Item("2017-01-10", label="Creation Time"), Descriptions.Item("2017-10-10", label="Effective Time"), Descriptions.Item("Gonghu Road, Xihu District, Hangzhou, Zhejiang, China", label="Remarks")], size="small", column=3),
 br(),
 PageHeader("Running", onBack=lambda :window.history.back(), title="Title", tags="{<Tag color=", blue"=True),
 Button("Operation", key="3"),
 Button("Operation", key="2"),
 Button("Primary", key="1", type="primary"),
 Row([Statistic(title="Status", value="Pending"), Statistic(title="Price", prefix="$", value=568.08, style=dict(margin='0 32px')), Statistic(title="Balance", prefix="$", value=3345.08)]),
]