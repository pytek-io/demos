from render_html import *
from render_antd import Rate
value = this.value
def app():
    return span([Rate(tooltips=desc, onChange=this.handleChange, value=value), ""{value ?", span(""{desc[value - 1]}"", className="ant-rate-text"), ": ''}""])
def app():
    return Rater()