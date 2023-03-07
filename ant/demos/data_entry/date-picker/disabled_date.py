import datetime

import reflect_antd as antd

RangePicker = antd.DatePicker.RangePicker


disabledDate = r.js_arrow(
    "disabledDate",
    """(current) => current && current < dayjs().endOf('day')""",
)

disabledDateTime = r.js_arrow(
    "disabledDateTime",
    """() => {
    const range = (start, end) => {
        const result = [];
        for (let i = start; i < end; i++) {
            result.push(i);
        }
        return result;
    };
    return {
        disabledHours: () => range(0, 24).splice(4, 20),
        disabledMinutes: () => range(30, 60),
        disabledSeconds: () => [55, 56],
    };
};
""",
)

disabledRangeTime = r.js_arrow(
    "disabledRangeTime",
    """(_, type) => {
      range = (start, end) => {
        result = [];
        for (let i = start; i < end; i++) {
          result.push(i);
        }
        return result;
      };
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
                disabledTime=disabledRangeTime,
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
