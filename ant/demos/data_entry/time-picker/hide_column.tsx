import { TimePicker } from 'antd';
import moment from 'moment';

const format = 'HH:mm';

ReactDOM.render(<TimePicker defaultValue={moment('12:08', format)} format={format} />, mountNode);