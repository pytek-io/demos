from render_antd import Select
from render_html import *

Option = Select.Option
def app():
    return[
 Select([""{provinceData.map(provinclambda e:(", Option(""{province}"", key=province), "))}""], defaultValue=provinceData[0], style=dict(width=120), onChange=handleProvinceChange),
 Select([""{cities.map(city => (", Option(""{city}"", key=city), "))}""], style=dict(width=120), value=secondCity, onChange=onSecondCityChange),
]
def app():
    return App()