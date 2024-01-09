from render_antd import Calendar, Col, Radio, Row, Select, Typography
from render_html import *


def headerRender(value, type, onChange, onTypeChange):
    start = 0
    end = 12
    monthOptions = []

    current = value.clone()
    localeData = value.localeData()
    months = []
    for i in range(12):
        current.month(i)
        months.push(localeData.monthsShort(current))

    for index in range(start, end):
        monthOptions.append(object)(
            Select.Option(months[index], className="month-item", key=index)
        )
    month = value.month()
    year = value.year()
    options = []
    for i in range(year - 10, year + 10):
        options.push(Select.Option(i, key=i, value=i, className="year-item"))


def app():
    return (
        div(
            [
                Typography.Title("Custom header", level=4),
                Row(
                    [
                        Col(
                            Radio.Group(
                                [
                                    Radio.Button("Month", value="month"),
                                    Radio.Button("Year", value="year"),
                                ],
                                size="small",
                                onChange=lambda e: onTypeChange(e.target.value),
                                value=type,
                            )
                        ),
                        Col(
                            Select(
                                "{options}",
                                size="small",
                                dropdownMatchSelectWidth=False,
                                className="my-year-select",
                                value=String(year),
                            )
                        ),
                        Col(
                            Select(
                                "{monthOptions}",
                                size="small",
                                dropdownMatchSelectWidth=False,
                                value=String(month),
                            )
                        ),
                    ],
                    gutter=8,
                ),
            ],
            style=dict(padding=8),
        ),
    )
