from render_antd import Popover, Steps
from render_html import *

Step = Steps.Step
customDot = Popover("}"   >     "{dot}"", content="{       <span>         step ", {index}"=True, status:=True, "{status}"=True, <=True, span=True)
def app(_):
    return Steps([Step(title="Finished", description="You can hover on the dot."), Step(title="In Progress", description="You can hover on the dot."), Step(title="Waiting", description="You can hover on the dot."), Step(title="Waiting", description="You can hover on the dot.")], current=1, progressDot=customDot)