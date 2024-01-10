from render_antd import Button, Form, Mentions
from render_html import *

Option, getMentions = Mentions.Option, Mentions.getMentions
onReset = Form([Form.Item(Mentions([Option("afc163", value="afc163"), Option("zombieJ", value="zombieJ"), Option("yesmeck", value="yesmeck")], rows=1), name="coders", label="Top coders", labelCol=dict(span=6), wrapperCol=dict(span=16), rules="{[", {=True, validator:=True, checkMention=True, }"]}"=True), Form.Item(Mentions([Option("afc163", value="afc163"), Option("zombieJ", value="zombieJ"), Option("yesmeck", value="yesmeck")], rows=3, placeholder="You can use @ to ref user here"), name="bio", label="Bio", labelCol=dict(span=6), wrapperCol=dict(span=16), rules="{[", {=True, required:=True, true=True, }"]}"=True), Form.Item([Button("Submit", htmlType="submit", type="primary"), Button("Reset", htmlType="button", onClick=onReset)], wrapperCol=dict(span=14, offset=6))], form=form, layout="horizontal", onFinish=onFinish)
def app(_):
    return App()