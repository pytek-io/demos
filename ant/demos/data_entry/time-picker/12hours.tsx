import { TimePicker } from 'antd';

function onChange(time, timeString) {
  console.log(time, timeString);
}

ReactDOM.render(
  <>
    <TimePicker use12Hours onChange={onChange} />
    <TimePicker use12Hours format="h:mm:ss A" onChange={onChange} style={{ width: 140 }} />
    <TimePicker use12Hours format="h:mm a" onChange={onChange} />
  </>,
  mountNode,
);