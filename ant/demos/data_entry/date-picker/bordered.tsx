import { DatePicker, Space } from 'antd';

const { RangePicker } = DatePicker;

ReactDOM.render(
  <Space direction="vertical" size={12}>
    <DatePicker bordered={false} />
    <DatePicker picker="week" bordered={false} />
    <DatePicker picker="month" bordered={false} />
    <DatePicker picker="year" bordered={false} />
    <RangePicker bordered={false} />
    <RangePicker picker="week" bordered={false} />
    <RangePicker picker="month" bordered={false} />
    <RangePicker picker="year" bordered={false} />
  </Space>,
  mountNode,
);