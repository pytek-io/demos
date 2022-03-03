from reflect_html import *
from reflect_antd import Mentions
Option = Mentions.Option
search = this.search
users, loading = this.users, this.loading
def app():
    return Mentions([""{users.map(( login, avatar_url: avatar ) => (", Option([img(src=avatar, alt=login), span(""{login}"")], key=login, value=login, className="antd-demo-dynamic-option"), "))}""], style=dict(width='100%'), loading=loading, onSearch=this.onSearch)
def app():
    return AsyncMention()