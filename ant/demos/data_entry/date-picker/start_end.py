import datetime

import reflect as r
import reflect_antd as antd

greater_dates = r.js_arrow("greater_dates", "(date1, date2) => date2 > date1")
less_dates = r.js_arrow("lesser_dates", "(date1, date2) => date2 < date1")


def app():
    start_value = r.ObservableValue(datetime.datetime.now())
    end_value = r.ObservableValue(datetime.datetime.now() + datetime.timedelta(days=15))
    return antd.Row(
        [
            antd.Col(
                antd.DatePicker(
                    disabledDate=greater_dates(end_value()),
                    format="YYYY-MM-DD",
                    value=start_value,
                    placeholder="Start",
                )
            ),
            antd.Col(
                antd.DatePicker(
                    disabledDate=less_dates(start_value()),
                    format="YYYY-MM-DD",
                    value=end_value,
                    placeholder="End",
                )
            ),
        ],
        gutter=20,
    )
