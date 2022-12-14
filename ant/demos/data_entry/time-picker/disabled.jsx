import { TimePicker } from 'antd';
import moment from 'moment';

ReactDOM.render(<TimePicker defaultValue={moment('12:08:23', 'HH:mm:ss')} disabled />, mountNode);