import { Spin, Space } from 'antd';

ReactDOM.render(
  <Space size="middle">
    <Spin size="small" />
    <Spin />
    <Spin size="large" />
  </Space>,
  mountNode,
);