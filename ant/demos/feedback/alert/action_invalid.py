from render_antd import Alert, Button, Space
from render_html import *


def app():
    return[
 Alert("UNDO", message="Success Tips", type="success", showIcon=True, action="{         <Button size=", small"=True, type="text"),
 Alert("Detail", message="Error Text", showIcon=True, description="Error Description Error Description Error Description Error Description", type="error", action="{         <Button size=", small"=True, danger=True),
 Alert("Done", message="Warning Text", type="warning", action="{         <Space>           <Button size=", small"=True, type="ghost"),
 Alert([Button("Accept", size="small", type="primary"), Button("Decline", size="small", danger=True, type="ghost")], message="Info Text", description="Info Description Info Description Info Description Info Description", type="info", action="{         <Space direction=", vertical"=True),
]