import { TimePicker } from 'antd';
import moment from 'moment';
import { SmileOutlined } from '@ant-design/icons';

function onChange(time, timeString) {
  console.log(time, timeString);
}

ReactDOM.render(
  <TimePicker
    suffixIcon={<SmileOutlined />}
    onChange={onChange}
    defaultOpenValue={moment('00:00:00', 'HH:mm:ss')}
  />,
  mountNode,
);