import { DatePicker, Space } from 'antd';

const { RangePicker } = DatePicker;

ReactDOM.render(
  <Space direction="vertical" size={12}>
    <RangePicker />
    <RangePicker showTime />
    <RangePicker picker="week" />
    <RangePicker picker="month" />
    <RangePicker picker="year" />
  </Space>,
  mountNode,
);