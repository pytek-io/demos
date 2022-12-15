import { TimePicker } from 'antd';

const { RangePicker } = TimePicker;

ReactDOM.render(
  <>
    <TimePicker bordered={false} />
    <RangePicker bordered={false} />
  </>,
  mountNode,
);