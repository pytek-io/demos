import { Badge } from 'antd';
import { NotificationOutlined } from '@ant-design/icons';

ReactDOM.render(
  <div>
    <Badge dot>
      <NotificationOutlined />
    </Badge>
    <Badge count={0} dot>
      <NotificationOutlined />
    </Badge>
    <Badge dot>
      <a href="#">Link something</a>
    </Badge>
  </div>,
  mountNode,
);