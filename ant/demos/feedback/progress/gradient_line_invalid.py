from reflect_html import *
from reflect_antd import Progress
def app():
    return[
 Progress(strokeColor=dict('0%'='#108ee9', '100%'='#87d068'), percent=99.9),
 Progress(strokeColor=dict(from='#108ee9', to='#87d068'), percent=99.9, status="active"),
 Progress(type="circle", strokeColor=dict('0%'='#108ee9', '100%'='#87d068'), percent=90),
 Progress(type="circle", strokeColor=dict('0%'='#108ee9', '100%'='#87d068'), percent=100),
]
def app():
    return Demo()