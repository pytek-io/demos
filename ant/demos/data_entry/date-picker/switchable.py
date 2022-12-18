import reflect_antd as antd


def picker_with_type(picker_type, onChange):
    if picker_type() == "time":
        return antd.TimePicker(onChange=onChange)
    if picker_type() == "date":
        return antd.DatePicker(onChange=onChange)
    return antd.DatePicker(picker=picker_type, onChange=onChange)


def app():
    picker_type = antd.Select(
        options=[
            {"label": "Time", "value": "time"},
            {"label": "Date", "value": "date"},
            {"label": "Week", "value": "week"},
            {"label": "Month", "value": "month"},
            {"label": "Quarter", "value": "quarter"},
            {"label": "Year", "value": "year"},
        ],
        defaultValue="time",
    )
    return antd.Space(
        [
            picker_type,
            lambda: picker_with_type(picker_type=picker_type, onChange=print),
        ],
        direction="vertical",
    )
