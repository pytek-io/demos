import { TimePicker } from 'antd';
import moment from 'moment';

function onChange(time, timeString) {
  console.log(time, timeString);
}

ReactDOM.render(
  <TimePicker onChange={onChange} defaultOpenValue={moment('00:00:00', 'HH:mm:ss')} />,
  mountNode,
);