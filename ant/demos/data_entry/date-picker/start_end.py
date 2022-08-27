from reflect_antd import DatePicker, Row, Col
from reflect import create_observable
from reflect import JSMethod
from datetime import datetime, timedelta


compare_dates = JSMethod(
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
    start_value = create_observable(datetime.now())
    end_value = create_observable(datetime.now() + timedelta(days=15))

    return Row(
        [
            Col(
                DatePicker(
                    disabledDate=compare_dates(end_value(), True),
                    format="YYYY-MM-DD",
                    value=start_value,
                    placeholder="Start",
                )
            ),
            Col(
                DatePicker(
                    disabledDate=compare_dates(start_value(), False),
                    format="YYYY-MM-DD",
                    value=end_value,
                    placeholder="End",
                )
            ),
        ],
        gutter=20,
    )
