import datetime

import reflect as r
import reflect_antd as antd

compare_dates = r.JSMethod(
    "compare_dates",
    """{
        console.log(date1, date2)
        let result = date2.getTime() > date1.getTime();
        return greater ? result : !result;
    }""",
    "date1",
    "greater",
    "date2",
)


def app():
    start_value = r.ObservableValue(datetime.datetime.now())
    end_value = r.ObservableValue(datetime.datetime.now() + datetime.timedelta(days=15))
    return antd.Row(
        [
            antd.Col(
                antd.DatePicker(
                    disabledDate=compare_dates(end_value(), True),
                    format="YYYY-MM-DD",
                    value=start_value,
                    placeholder="Start",
                )
            ),
            antd.Col(
                antd.DatePicker(
                    disabledDate=compare_dates(start_value(), False),
                    format="YYYY-MM-DD",
                    value=end_value,
                    placeholder="End",
                )
            ),
        ],
        gutter=20,
    )
