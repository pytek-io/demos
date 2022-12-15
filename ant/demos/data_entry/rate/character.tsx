import { Rate } from 'antd';
import { HeartOutlined } from '@ant-design/icons';

ReactDOM.render(
  <>
    <Rate character={<HeartOutlined />} allowHalf />
    <br />
    <Rate character="A" allowHalf style={{ fontSize: 36 }} />
    <br />
    <Rate character="好" allowHalf />
  </>,
  mountNode,
);