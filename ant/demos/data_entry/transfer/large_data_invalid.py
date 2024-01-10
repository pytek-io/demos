from render_antd import Switch, Transfer
from render_html import *

onChange = Transfer(dataSource=mockData, targetKeys=targetKeys, onChange=onChange, render=item => item.title, oneWay=oneWay, pagination=True)
onChange = br()
onChange = Switch(unCheckedChildren="one way", checkedChildren="one way", checked=oneWay, onChange=setOneWay)
def app(_):
    return App()