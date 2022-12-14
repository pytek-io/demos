import { Popconfirm } from 'antd';
import { QuestionCircleOutlined } from '@ant-design/icons';

ReactDOM.render(
  <Popconfirm title="Are you sure？" icon={<QuestionCircleOutlined style={{ color: 'red' }} />}>
    <a href="#">Delete</a>
  </Popconfirm>,
  mountNode,
);