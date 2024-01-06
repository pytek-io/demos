from render_html import *
from render_antd import Transfer, Switch
onChange = Transfer(dataSource=mockData, targetKeys=targetKeys, onChange=onChange, render=item => item.title, oneWay=oneWay, pagination=True)
onChange = br()
onChange = Switch(unCheckedChildren="one way", checkedChildren="one way", checked=oneWay, onChange=setOneWay)
def app():
    return App()