"""
A Render version of an app created created using three different web frameworks ( 
https://www.youtube.com/watch?v=3vfum74ggHE). The corresponding code can be found under(
https://github.com/python-engineer/python-fun/tree/master/webapps). Note that the style is a bit 
off as we use Ant components. It demonstrates how one can combine an ORM such as sql alchemy 
with Render.
"""
import render as r
import render_antd as antd
import render_html as html
import sqlalchemy

TITLE = "Todo App"
CSS = ["https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css"]
Base = sqlalchemy.orm.declarative_base()


class Todo(Base):
    __tablename__ = "todo"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(100))
    complete = sqlalchemy.Column(sqlalchemy.Boolean)


def app(_):
    def add_todo():
        todo = Todo(title=title(), complete=False)
        session.add(todo)
        todos.append(todo)
        title.set("")
        session.commit()

    def delete_todos(todo):
        todos.remove(todo)
        session.delete(todo.back_ref)
        session.commit()

    def update_todo(todo):
        todo.complete = not todo.complete()
        session.commit()

    engine = sqlalchemy.create_engine("sqlite+pysqlite:///db.sqlite:", future=True)
    Base.metadata.create_all(engine)
    session = sqlalchemy.orm.Session(engine).__enter__()
    title = antd.Input(
        placeholder="Enter Todo...", onPressEnter=add_todo, style={"marginBottom": 12}
    )
    todos = r.create_observable(session.query(Todo).all(), depth=3)

    def create_todo_row(todo):
        return html.div(
            [
                html.p(f"{todo.id()}|{todo.title()}", className="ui big header"),
                html.br(),
                lambda: html.span("Complete", className="ui green label")
                if todo.complete()
                else html.span("Not Complete", className="ui gray label"),
                antd.Button(
                    "Update",
                    className="ui blue button",
                    onClick=lambda: update_todo(todo),
                ),
                antd.Button(
                    "Delete",
                    className="ui red button",
                    onClick=lambda: delete_todos(todo),
                ),
            ],
            style={"display": "block", "verticalAlign": "middle"},
            className="ui segment",
        )

    return html.div(
        [
            html.h1("To Do App", className="ui center aligned header"),
            html.div([html.label("Todo Title"), title, html.br()], className="field"),
            antd.Button("Add", className="ui blue button", onClick=add_todo),
            html.hr(),
            html.div(r.Mapping(create_todo_row, todos, evaluate_argument=False)),
        ],
        style={"marginTop": "50px"},
        className="ui container",
    )
