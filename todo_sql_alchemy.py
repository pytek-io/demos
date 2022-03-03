"""
A Reflect version of https://www.youtube.com/watch?v=3vfum74ggHE. Note that the style is a bit 
off as we use Ant components. It demonstrates how one can combine an ORM such as sql alchemy 
with Reflect.
"""
from reflect_html import div, h1, label, p, br, span, hr
from reflect_antd import Input, Button
from reflect import make_observable, Mapping
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, Session

TITLE = "Todo App"
CSS = ["https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css"]
Base = declarative_base()


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    complete = Column(Boolean)


def app():
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

    engine = create_engine("sqlite+pysqlite:///db.sqlite:", future=True)
    Base.metadata.create_all(engine)
    session = Session(engine).__enter__()
    title = Input(
        placeholder="Enter Todo...", onPressEnter=add_todo, style={"marginBottom": 12}
    )
    todos = make_observable(session.query(Todo).all(), depth=3)

    def create_todo_row(todo):
        return div(
            [
                p(f"{todo.id()}|{todo.title()}", className="ui big header"),
                br(),
                lambda: span("Complete", className="ui green label")
                if todo.complete()
                else span("Not Complete", className="ui gray label"),
                Button(
                    "Update",
                    className="ui blue button",
                    onClick=lambda: update_todo(todo),
                ),
                Button(
                    "Delete",
                    className="ui red button",
                    onClick=lambda: delete_todos(todo),
                ),
            ],
            style={"display": "block", "verticalAlign": "middle"},
            className="ui segment",
        )

    return div(
        [
            h1("To Do App", className="ui center aligned header"),
            div([label("Todo Title"), title, br()], className="field"),
            Button("Add", className="ui blue button", onClick=add_todo),
            hr(),
            div(Mapping(create_todo_row, todos)),
        ],
        style={"marginTop": "50px"},
        className="ui container",
    )
