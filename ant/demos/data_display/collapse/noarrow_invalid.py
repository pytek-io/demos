from render_html import *
from render_antd import Collapse
Panel = Collapse.Panel
def app():
    return Collapse([Panel(p(""{text}""), header="This is panel header with arrow icon", key="1"), Panel(p(""{text}""), showArrow=False, header="This is panel header with no arrow icon", key="2")], defaultActiveKey=['1'], onChange=callback)