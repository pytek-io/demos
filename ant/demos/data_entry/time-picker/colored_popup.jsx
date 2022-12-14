import { TimePicker } from 'antd';
import moment from 'moment';

const onChange = (time, timeString) => {
  console.log(time, timeString);
};

ReactDOM.render(
  <TimePicker
    onChange={onChange}
    defaultOpenValue={moment('00:00:00', 'HH:mm:ss')}
    popupClassName="myCustomClassName"
  />,
  mountNode,
);