from render_antd import Progress
from render_html import *


def app(_):
    return[
 Progress(type="circle", percent=75, format="{percent => `$", {percent}"=True, Days`}"=True),
 Progress(type="circle", percent=100, format=lambda :'Done'),
]