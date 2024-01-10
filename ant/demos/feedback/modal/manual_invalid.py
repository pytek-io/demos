import 'antd'
import Button }
import { Modal
from render_antd import Button, Modal
from render_html import *

# def countDown():
#   secondsToGo = 5;
#   modal = Modal.success({
#     title: 'This is a notification message',
#     content: `This modal will be destroyed after ${secondsToGo} second.`,
#   });
#   const timer = setInterval(() => {
#     secondsToGo -= 1;
#     modal.update({
#       content: `This modal will be destroyed after ${secondsToGo} second.`,
#     });
#   }, 1000);
#   setTimeout(() => {
#     clearInterval(timer);
#     modal.destroy();
#   }, secondsToGo * 1000);
# }

# ReactDOM.render(<Button onClick={countDown}>Open modal to close in 5s</Button>, mountNode);
def app(_):
    return Button("Open modal to close in 5s", 
    onClick=countDown)
