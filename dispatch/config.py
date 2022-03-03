from reflect import js
from reflect_utils.formatters import (
    compose,
    durationFormatter,
    filesize,
    hexadecimalFormatter,
    numeral,
    percentage,
    pythonTimeStampToJSDate,
    replace_value,
    round_value,
    toLocaleDateString,
    toLocaleTimeString,
    transform_if_number,
)

CLIENT = 1
WORKER = 2
PRIORITY_GROUP = 3
DEPLOYMENT = 4
SESSION = 5
SAFE_MAX_INTEGER = 4503599627370495

blank_zeros = replace_value(numeral)
blank_infinity = replace_value(numeral, SAFE_MAX_INTEGER)
pythonTimeStampFormatter = compose(pythonTimeStampToJSDate, toLocaleTimeString)

runningTasksColumnDefs = [
    {"headerName": "Uid", "field": "id", "width": 70, "sortable": True},
    {
        "headerName": "Worker Uid",
        "field": "worker_id",
        "width": 70,
        "sortable": True,
        "valueNumberFormatter": hexadecimalFormatter,
    },
    {
        "headerName": "Start Time",
        "field": "start",
        "valueValueFormatter": pythonTimeStampFormatter,
        "width": 100,
        "sortable": True,
    },
    {
        "headerName": "Expected Duration",
        "field": "expected_duration",
        "width": 90,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "valueValueFormatter": durationFormatter,
    },
    {
        "headerName": "Overrun Tolerance (%)",
        "field": "overrun_tolerance",
        "width": 90,
        "cellStyle": {"textAlign": "right"},
        "valueNumberFormatter": percentage,
        "sortable": True,
    },
    {
        "headerName": "Maximum memory",
        "field": "max_memory",
        "width": 90,
        "cellStyle": {"textAlign": "right"},
        "valueNumberFormatter": filesize,
        "sortable": True,
    },
    {
        "headerName": "Description",
        "field": "description",
        "width": 140,
        "sortable": True,
    },
]

session_menu_items = [
    dict(
        name="Cancel",
        confirmation="Are you sure you want to cancel this deployment?",
        action_tag="DeleteDeployment",
    ),
]


RUNNING_TASKS_DEF = {
    "name": "Sessions",
    "static_fields": [
        "worker_id",
        "start",
        "expected_duration",
        "overrun_tolerance",
        "max_memory",
        "task_or_command",
        "description",
    ],
    "update_fields": [],
    "columns": runningTasksColumnDefs,
    "getContextMenuItems": session_menu_items,
}


round_value_to_two_digits = transform_if_number(round_value(2))

creationDateTimeColumnDef = {
    "headerName": "Creation Date",
    "field": "creation_time",
    "valueValueFormatter": compose(pythonTimeStampToJSDate, toLocaleDateString),
    "width": 110,
    "sortable": True,
    "aggFunc": js("constant", None),
}

creationTimeColumnDef = {
    "headerName": "Creation Time",
    "field": "creation_time",
    "valueValueFormatter": pythonTimeStampFormatter,
    "width": 100,
    "sortable": True,
}

deployments_columns = [
    {
        "headerName": "Uid",
        "field": "id",
        "width": 90,
        "sortable": True,
        "valueNumberFormatter": hexadecimalFormatter,
    },
    creationDateTimeColumnDef,
    {
        "headerName": "Size",
        "field": "size",
        "width": 80,
        "sortable": True,
        "cellStyle": {"textAlign": "right"},
        "valueNumberFormatter": filesize,
    },
    {"headerName": "Tags", "field": "tags", "width": 110, "sortable": True},
    {
        "headerName": "Description",
        "field": "description",
        "width": 220,
        "sortable": True,
    },
]

worker_columns = [
    {
        "headerName": "Uid",
        "field": "id",
        "width": 70,
    },
    {"headerName": "Host", "field": "host_name", "width": 200, "sortable": True},
    {"headerName": "Name", "field": "name", "width": 200, "sortable": True},
    {
        "headerName": "tasks",
        "field": "nb_tasks",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
    },
    {
        "headerName": "Load averages (mins)",
        "children": [
            {
                "headerName": "1",
                "field": "loadavg_1",
                "width": 80,
                "cellStyle": {"textAlign": "right"},
                "sortable": True,
                "valueFormatter": round_value_to_two_digits,
            },
            {
                "headerName": "5",
                "field": "loadavg_5",
                "width": 80,
                "cellStyle": {"textAlign": "right"},
                "sortable": True,
                "valueFormatter": round_value_to_two_digits,
            },
            {
                "headerName": "15",
                "field": "loadavg_15",
                "width": 80,
                "cellStyle": {"textAlign": "right"},
                "sortable": True,
                "valueFormatter": round_value_to_two_digits,
            },
        ],
    },
    {
        "headerName": "PID",
        "field": "pid",
        "width": 70,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
    },
    {
        "headerName": "cores",
        "field": "nb_cores",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
    },
    {
        "headerName": "slaves",
        "field": "nb_slaves",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
    },
]

client_columns = [
    {
        "headerName": "Uid",
        "field": "id",
        "width": 70,
        "valueNumberFormatter": hexadecimalFormatter,
    },
    {"headerName": "Host", "field": "host", "width": 200, "sortable": True},
    {"headerName": "User", "field": "user", "width": 200, "sortable": True},
    {
        "headerName": "PID",
        "field": "pid",
        "width": 70,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
    },
    {
        "headerName": "Description",
        "field": "description",
        "width": 140,
        "sortable": True,
    },
]

editable = {
    "editable": True,
    "enableCellChangeFlash": True,
    "onCellValueChanged": js("onDispatchCellValueChanged"),
    "singleClickEdit": True,
}


def make_editable(definition):
    return dict(definition.items(), **editable)


tasks_counts = [
    {
        "headerName": "Pending",
        "field": "nb_tasks_pending",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "enableCellChangeFlash": True,
        "valueValueFormatter": blank_zeros,
        "aggFunc": "sum",
    },
    {
        "headerName": "Ready",
        "field": "nb_tasks_ready",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "enableCellChangeFlash": True,
        "valueValueFormatter": blank_zeros,
        "aggFunc": "sum",
    },
    {
        "headerName": "Running",
        "field": "nb_tasks_running",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "enableCellChangeFlash": True,
        "valueValueFormatter": blank_zeros,
        "aggFunc": "sum",
    },
    {
        "headerName": "Complete",
        "field": "nb_tasks_complete",
        "width": 90,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "enableCellChangeFlash": True,
        "valueValueFormatter": blank_zeros,
        "aggFunc": "sum",
    },
]

tasks_durations = [
    {
        "headerName": "Pending",
        "hide": True,
        "field": "duration_pending",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "valueValueFormatter": durationFormatter,
        "aggFunc": "sum",
    },
    {
        "headerName": "Ready",
        "hide": True,
        "field": "duration_ready",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "valueValueFormatter": durationFormatter,
        "aggFunc": "sum",
    },
    {
        "headerName": "Running",
        "hide": True,
        "field": "duration_running",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "valueValueFormatter": durationFormatter,
        "aggFunc": "sum",
    },
    {
        "headerName": "Complete",
        "hide": True,
        "field": "duration_complete",
        "width": 90,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "valueValueFormatter": durationFormatter,
        "aggFunc": "sum",
    },
]

dataSizeColumn = {
    "width": 120,
    "cellStyle": {"textAlign": "right"},
    "sortable": True,
    "aggFunc": "sum",
    "valueValueFormatter": filesize,
}

input_size = dict(dataSizeColumn, headerName="Input", field="input_size")
output_size = dict(dataSizeColumn, headerName="Output", field="output_size")

session_columns = [
    make_editable(
        {
            "headerName": "Priority",
            "field": "priority",
            "width": 80,
            "cellStyle": {"textAlign": "right"},
            "sortable": True,
            "valueValueFormatter": blank_zeros,
        }
    ),
    {
        "headerName": "Slave Allocation",
        "children": [
            make_editable(
                {
                    "headerName": "Min",
                    "field": "min_slaves",
                    "width": 110,
                    "sortable": True,
                    "valueValueFormatter": blank_zeros,
                }
            ),
            make_editable(
                {
                    "headerName": "Max",
                    "field": "max_slaves",
                    "width": 110,
                    "sortable": True,
                    "valueValueFormatter": blank_infinity,
                }
            ),
        ],
    },
    {"headerName": "Task counts", "children": tasks_counts},
    {"headerName": "Task durations", "children": tasks_durations},
    {"headerName": "IO", "children": [input_size, output_size]},
    creationTimeColumnDef,
    {
        "headerName": "ETA",
        "field": "eta",
        "valueNumberFormatter": pythonTimeStampFormatter,
        "width": 100,
        "sortable": True,
    },
    {
        "headerName": "Context Size",
        "field": "context_size",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "valueNumberFormatter": filesize,
    },
    {"headerName": "User", "field": "user", "width": 100, "sortable": True},
    {
        "headerName": "Deployment",
        "children": [
            {
                "headerName": "Tag",
                "field": "deployment_tag",
                "width": 110,
                "sortable": True,
            },
            {
                "headerName": "Uid",
                "field": "deployment_id",
                "valueValueFormatter": replace_value(hexadecimalFormatter),
                "width": 110,
                "sortable": True,
            },
        ],
    },
    {
        "headerName": "Client Uid",
        "field": "client_id",
        "valueNumberFormatter": hexadecimalFormatter,
        "hide": True,
    },
    {
        "headerName": "Uid",
        "field": "id",
        "width": 70,
        "hide": False,
        "valueFormatter": replace_value(hexadecimalFormatter),
    },
    {
        "headerName": "Description",
        "field": "description",
        "width": 140,
        "sortable": True,
    },
]

WORKER_DEF = {
    "name": "Workers",
    "static_fields": ["nb_cores", "nb_slaves", "host_name", "name", "pid"],
    "update_fields": ["nb_tasks", "loadavg_1", "loadavg_5", "loadavg_15"],
    "columns": worker_columns,
}

CLIENT_DEF = {
    "name": "Clients",
    "static_fields": ["user", "host", "pid", "description"],
    "update_fields": [],
    "columns": client_columns,
}

# not sure why do we send deployment updates
deployment_fields = ["description", "tags", "creation_time", "size"]

deployment_menu_items = [
    dict(
        name="Delete",
        confirmation="Are you sure you want to delete this deployment?",
        action_tag="DeleteDeployment",
    ),
]

DEPLOYMENT_DEF = {
    "name": "Deployments",
    "static_fields": deployment_fields,
    "update_fields": deployment_fields,
    "columns": deployments_columns,
    "getContextMenuItems": deployment_menu_items,
}

session_menu_items = [
    dict(
        name="Cancel",
        confirmation="Are you sure you want to cancel this session?",
        action_tag="TerminateSession",
    ),
    dict(
        name="Display running tasks",
        action_tag="DisplayRunningTasks",
    ),
]

SESSION_DEF = {
    "name": "Sessions",
    "static_fields": [
        "is_session",
        "deployment_id",
        "deployment_tag",
        "description",
        "user",
        "client_id",
        "priority_group_path",
        "creation_time",
        "context_size",
    ],
    "update_fields": [
        "priority",
        "nb_tasks_pending",
        "nb_tasks_ready",
        "nb_tasks_running",
        "nb_tasks_complete",
        "duration_pending",
        "duration_ready",
        "duration_running",
        "duration_complete",
        "output_size",
        "input_size",
        "min_slaves",
        "max_slaves",
        "eta",
    ],
    "columns": session_columns,
    "getContextMenuItems": session_menu_items,
}

DEFINITIONS = {
    WORKER: WORKER_DEF,
    CLIENT: CLIENT_DEF,
    DEPLOYMENT: DEPLOYMENT_DEF,
    SESSION: SESSION_DEF,
}
