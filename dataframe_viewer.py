import json
import pandas as pd
import pathlib
from os.path import join
from reflect import get_window, make_observable
from reflect_aggrid import AgGridColumn, AgGridReact, ColumnDetails
from reflect_antd import Button, Col, Row
from reflect_html import div
from reflect_utils.common import create_file_chooser
import reflect_utils.formatters  # this will import the formatters (we might want to move this reflect_aggrid...)



def content(application_path=None):
    application_arguments = lambda: (
        json.loads(application_path()) if application_path() else {}
    )

    def update_application_path(**kwargs):
        value = application_arguments()
        value.update(**kwargs)
        application_path.set(json.dumps(value))

    parent_folder = pathlib.Path(__file__).parent
    dimensions = make_observable((0, 0))
    file_selection_window, show_file_selection_window = create_file_chooser(
        title="Select file to open",
        on_ok=lambda path: update_application_path(file=path),
        base_path=parent_folder,
    )
    settings_selection_window, show_settings_selection_window = create_file_chooser(
        title="Select column settings to open",
        on_ok=lambda path: update_application_path(settings=path),
        base_path=parent_folder,
    )

    def file_name_from_hash():
        if application_arguments():
            return application_arguments()["file"]

    def description():
        if file_name_from_hash():
            nb_rows, nb_cols = dimensions()
            return f"{file_name_from_hash()} ({nb_rows} rows, {nb_cols} cols)"

    settings = Row(
        [
            Col(Button("Open", onClick=show_file_selection_window)),
            file_selection_window,
            Col(div(description, style=dict(paddingTop=3))),
            Col(Button("Settings", onClick=show_settings_selection_window)),
            settings_selection_window,
        ],
        gutter=20,
    )

    def column_details():
        arguments = application_arguments()
        settings = arguments.get("settings", None)
        if settings:
            return [
                ColumnDetails(**row)
                for row in json.loads(open(join(parent_folder, settings), "r").read())
            ]

    def create_grid():
        file_name = file_name_from_hash()
        if not file_name:
            return AgGridReact([], rowData=[], className="ag-theme-balham")
        path = join(parent_folder, file_name)
        extension = file_name.rsplit(".", 1)[-1]
        if extension == "csv":
            df = pd.read_csv(path)
        elif extension == "pick":
            df = pd.read_pickle(path)
        else:
            raise Exception(f"unknown extension")
        assert isinstance(df, pd.DataFrame)
        dimensions.set(df.shape)
        grid = AgGridReact(
            column_details()
            or [AgGridColumn(headerName=name, field=name) for name in df.columns],
            rowData=df,
            rowHeight=24,
            className="ag-theme-balham",
            defaultColDef=dict(resizable=True, filter=True),
            componentDidMount=lambda: grid.autoSizeColumns(list(df.columns), True),
        )
        return grid

    return {
        "title": lambda: application_arguments().get("file", ""),
        "settings": settings,
        "content": create_grid,
    }


def app(**kwargs):
    window = get_window()
    app = content(window.hash)
    window.set_title(app["title"])
    return div(
        [
            Row(
                [Col(app["settings"])],
                gutter=20,
                style=dict(margin=10),
            ),
            div(
                app["content"],
                style=dict(height="calc(100% - 50px)"),
            ),
        ],
        style=dict(
            height="100%",
        ),
    )
