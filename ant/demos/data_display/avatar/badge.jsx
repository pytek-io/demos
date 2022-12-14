import { Avatar, Badge } from 'antd';
import { UserOutlined } from '@ant-design/icons';

ReactDOM.render(
  <>
    <span className="avatar-item">
      <Badge count={1}>
        <Avatar shape="square" icon={<UserOutlined />} />
      </Badge>
    </span>
    <span>
      <Badge dot>
        <Avatar shape="square" icon={<UserOutlined />} />
      </Badge>
    </span>
  </>,
  mountNode,
);