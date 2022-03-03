from reflect_html import *
from reflect_antd import Transfer
from reflect import js
mockData = [
    {
        "key": i,
        "title": f"content{i + 1}",
        "description": f"description of content{i + 1}",
    }
    for i in range(20)
]

initialTargetKeys = [item["key"] for item in mockData if item["key"] > 10]

def app():
    return Transfer(dataSource=mockData, 
    titles=['Source', 'Target'], 
    selectedKeys=selectedKeys, 
    onChange=onChange, 
    onSelectChange=onSelectChange, 
    onScroll=onScroll, 
    render=js("fetch_attribute", "title"))