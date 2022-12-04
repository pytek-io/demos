from reflect_html import *
from reflect_antd import List, Card
def app():
    return List("Card content", grid=dict(gutter=16, xs=1, sm=2, md=4, lg=4, xl=6, xxl=3), dataSource=data, renderItem="{item => (       <List.Item>         <Card title=", {item.title}"=True)