import reflect as r
import reflect_utils

CLIENT = 1
WORKER = 2
PRIORITY_GROUP = 3
DEPLOYMENT = 4
SESSION = 5
SAFE_MAX_INTEGER = 4503599627370495
blank_zeros = reflect_utils.replace_value(reflect_utils.numeral)
blank_infinity = reflect_utils.replace_value(reflect_utils.numeral, SAFE_MAX_INTEGER)
pythonTimeStampFormatter = reflect_utils.compose(
    reflect_utils.pythonTimeStampToJSDate, reflect_utils.toLocaleTimeString
)
from reflect_utils.formatters import apply_to_value

runningTasksColumnDefs = [
    {"headerName": "Uid", "field": "id", "width": 70, "sortable": True},
    {
        "headerName": "Worker Uid",
        "field": "worker_id",
        "width": 70,
        "sortable": True,
        "valueFormatter": reflect_utils.transform_if_number(
            reflect_utils.hexadecimalFormatter
        ),
    },
    {
        "headerName": "Start Time",
        "field": "start",
        "valueFormatter": apply_to_value(pythonTimeStampFormatter),
        "width": 100,
        "sortable": True,
    },
    {
        "headerName": "Expected Duration",
        "field": "expected_duration",
        "width": 90,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "valueFormatter": apply_to_value(reflect_utils.durationFormatter),
    },
    {
        "headerName": "Overrun Tolerance (%)",
        "field": "overrun_tolerance",
        "width": 90,
        "cellStyle": {"textAlign": "right"},
        "valueFormatter": reflect_utils.transform_if_number(reflect_utils.percentage),
        "sortable": True,
    },
    {
        "headerName": "Maximum memory",
        "field": "max_memory",
        "width": 90,
        "cellStyle": {"textAlign": "right"},
        "valueFormatter": reflect_utils.transform_if_number(reflect_utils.filesize),
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
    {
        "name": "Cancel",
        "confirmation": "Are you sure you want to cancel this deployment?",
        "action_tag": "DeleteDeployment",
    }
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
round_value_to_two_digits = reflect_utils.transform_if_number(
    reflect_utils.round_value(2)
)
creationDateTimeColumnDef = {
    "headerName": "Creation Date",
    "field": "creation_time",
    "valueFormatter": apply_to_value(
        reflect_utils.compose(
            reflect_utils.pythonTimeStampToJSDate, reflect_utils.toLocaleDateString
        )
    ),
    "width": 110,
    "sortable": True,
    "aggFunc": r.js("constant", None),
}
creationTimeColumnDef = {
    "headerName": "Creation Time",
    "field": "creation_time",
    "valueFormatter": apply_to_value(pythonTimeStampFormatter),
    "width": 100,
    "sortable": True,
}
deployments_columns = [
    {
        "headerName": "Uid",
        "field": "id",
        "width": 90,
        "sortable": True,
        "valueFormatter": reflect_utils.transform_if_number(
            reflect_utils.hexadecimalFormatter
        ),
    },
    creationDateTimeColumnDef,
    {
        "headerName": "Size",
        "field": "size",
        "width": 80,
        "sortable": True,
        "cellStyle": {"textAlign": "right"},
        "valueFormatter": reflect_utils.transform_if_number(reflect_utils.filesize),
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
    {"headerName": "Uid", "field": "id", "width": 70},
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
        "valueFormatter": reflect_utils.transform_if_number(
            reflect_utils.hexadecimalFormatter
        ),
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


tasks_counts = [
    {
        "headerName": "Pending",
        "field": "nb_tasks_pending",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "enableCellChangeFlash": True,
        "valueFormatter": apply_to_value(blank_zeros),
        "aggFunc": "sum",
    },
    {
        "headerName": "Ready",
        "field": "nb_tasks_ready",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "enableCellChangeFlash": True,
        "valueFormatter": apply_to_value(blank_zeros),
        "aggFunc": "sum",
    },
    {
        "headerName": "Running",
        "field": "nb_tasks_running",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "enableCellChangeFlash": True,
        "valueFormatter": apply_to_value(blank_zeros),
        "aggFunc": "sum",
    },
    {
        "headerName": "Complete",
        "field": "nb_tasks_complete",
        "width": 90,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "enableCellChangeFlash": True,
        "valueFormatter": apply_to_value(blank_zeros),
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
        "valueFormatter": apply_to_value(reflect_utils.durationFormatter),
        "aggFunc": "sum",
    },
    {
        "headerName": "Ready",
        "hide": True,
        "field": "duration_ready",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "valueFormatter": apply_to_value(reflect_utils.durationFormatter),
        "aggFunc": "sum",
    },
    {
        "headerName": "Running",
        "hide": True,
        "field": "duration_running",
        "width": 80,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "valueFormatter": apply_to_value(reflect_utils.durationFormatter),
        "aggFunc": "sum",
    },
    {
        "headerName": "Complete",
        "hide": True,
        "field": "duration_complete",
        "width": 90,
        "cellStyle": {"textAlign": "right"},
        "sortable": True,
        "valueFormatter": apply_to_value(reflect_utils.durationFormatter),
        "aggFunc": "sum",
    },
]
dataSizeColumn = {
    "width": 120,
    "cellStyle": {"textAlign": "right"},
    "sortable": True,
    "aggFunc": "sum",
    "valueFormatter": apply_to_value(reflect_utils.filesize),
}
input_size = dict(dataSizeColumn, headerName="Input", field="input_size")
output_size = dict(dataSizeColumn, headerName="Output", field="output_size")


def session_columns_definition(on_cell_change):
    def make_editable(definition):
        return dict(
            definition.items(),
            onCellValueChanged=on_cell_change(definition["field"]),
            editable=True,
            enableCellChangeFlash=True,
            singleClickEdit=True,
        )

    return [
        make_editable(
            {
                "headerName": "Priority",
                "field": "priority",
                "width": 80,
                "cellStyle": {"textAlign": "right"},
                "sortable": True,
                "valueFormatter": apply_to_value(blank_zeros),
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
                        "valueFormatter": apply_to_value(blank_zeros),
                    }
                ),
                make_editable(
                    {
                        "headerName": "Max",
                        "field": "max_slaves",
                        "width": 110,
                        "sortable": True,
                        "valueFormatter": apply_to_value(blank_infinity),
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
            "valueFormatter": reflect_utils.transform_if_number(
                pythonTimeStampFormatter
            ),
            "width": 100,
            "sortable": True,
        },
        {
            "headerName": "Context Size",
            "field": "context_size",
            "width": 80,
            "cellStyle": {"textAlign": "right"},
            "sortable": True,
            "valueFormatter": reflect_utils.transform_if_number(reflect_utils.filesize),
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
                    "valueFormatter": apply_to_value(
                        reflect_utils.replace_value(reflect_utils.hexadecimalFormatter)
                    ),
                    "width": 110,
                    "sortable": True,
                },
            ],
        },
        {
            "headerName": "Client Uid",
            "field": "client_id",
            "valueFormatter": reflect_utils.transform_if_number(
                reflect_utils.hexadecimalFormatter
            ),
            "hide": True,
        },
        {
            "headerName": "Uid",
            "field": "id",
            "width": 70,
            "hide": False,
            "valueFormatter": reflect_utils.replace_value(
                reflect_utils.hexadecimalFormatter
            ),
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
    "subject": WORKER,
    "static_fields": ["nb_cores", "nb_slaves", "host_name", "name", "pid"],
    "update_fields": ["nb_tasks", "loadavg_1", "loadavg_5", "loadavg_15"],
    "columns": worker_columns,
}
CLIENT_DEF = {
    "name": "Clients",
    "subject": CLIENT,
    "static_fields": ["user", "host", "pid", "description"],
    "update_fields": [],
    "columns": client_columns,
}
deployment_fields = ["description", "tags", "creation_time", "size"]
deployment_menu_items = [
    {
        "name": "Delete",
        "confirmation": "Are you sure you want to delete this deployment?",
        "action_tag": "DeleteDeployment",
    }
]
DEPLOYMENT_DEF = {
    "name": "Deployments",
    "subject": DEPLOYMENT,
    "static_fields": deployment_fields,
    "update_fields": deployment_fields,
    "columns": deployments_columns,
    "getContextMenuItems": deployment_menu_items,
}
session_menu_items = [
    {
        "name": "Cancel",
        "confirmation": "Are you sure you want to cancel this session?",
        "action_tag": "TerminateSession",
    },
    {"name": "Display running tasks", "action_tag": "DisplayRunningTasks"},
]


def create_session_columns(on_cell_change):
    return {
        "name": "Sessions",
        "subject": SESSION,
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
        "columns": session_columns_definition(on_cell_change),
        "getContextMenuItems": session_menu_items,
    }
