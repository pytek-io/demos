import reflect_antd as antd

import reflect as r


def picker_with_type(picker_type, onChange):
    if picker_type == "time":
        return antd.TimePicker(onChange=onChange)
    if picker_type == "date":
        return antd.DatePicker(onChange=onChange)
    return antd.DatePicker(picker=picker_type, onChange=onChange)


def app():
    picker_type = antd.Select(
        items=[
            {"children": "Time", "value": "time"},
            {"children": "Date", "value": "date"},
            {"children": "Week", "value": "week"},
            {"children": "Month", "value": "month"},
            {"children": "Quarter", "value": "quarter"},
            {"children": "Year", "value": "year"},
        ],
        defaultValue="time",
    )
    r.autorun(lambda: print(picker_type()))
    return antd.Space(
        [picker_type, picker_with_type(picker_type=picker_type, onChange=print)],
        direction="vertical",
    )
