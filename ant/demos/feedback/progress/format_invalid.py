from render_html import *
from render_antd import Progress
def app():
    return[
 Progress(type="circle", percent=75, format="{percent => `$", {percent}"=True, Days`}"=True),
 Progress(type="circle", percent=100, format=lambda :'Done'),
]