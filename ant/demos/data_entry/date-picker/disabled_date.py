import datetime

import reflect as r
import reflect_antd as antd

RangePicker = antd.DatePicker.RangePicker


disabledDate = r.JSMethod(
    "disabledDate", """return current && current < moment().endOf("day")""", "current"
)

disabledDateTime = r.JSMethod(
    "disabledDateTime",
    """return {
        disabledHours: () => range(0, 24).splice(4, 20),
        disabledMinutes: () => range(30, 60),
        disabledSeconds: () => [55, 56],
      };
    }""",
)

datePickerDisableRangeTime = r.JSMethod(
    "datePickerDisableRangeTime",
    """return {

    function disabledRangeTime(_, type) {
      if (type === "start") {
        return {
          disabledHours: () => range(0, 60).splice(4, 20),
          disabledMinutes: () => range(30, 60),
          disabledSeconds: () => [55, 56],
        };
      }
      return {
        disabledHours: () => range(0, 60).splice(20, 4),
        disabledMinutes: () => range(0, 31),
        disabledSeconds: () => [55, 56],
      };
    }""",
)


def app():
    return antd.Space(
        [
            antd.DatePicker(
                format="YYYY-MM-DD HH:mm:ss",
                disabledDate=disabledDate,
                disabledTime=disabledDateTime,
                showTime={"defaultValue": datetime.datetime.now()},
            ),
            antd.DatePicker(picker="month", disabledDate=disabledDate),
            RangePicker(disabledDate=disabledDate),
            RangePicker(
                disabledDate=disabledDate,
                disabledTime=datePickerDisableRangeTime,
                showTime={
                    "hideDisabledOptions": True,
                    "defaultValue": [
                        datetime.datetime.now(),
                        datetime.datetime.now() + datetime.timedelta(hours=12),
                    ],
                },
                format="YYYY-MM-DD HH:mm:ss",
            ),
        ],
        direction="vertical",
        size=12,
    )
