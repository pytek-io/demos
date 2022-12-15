import { Avatar } from 'antd';
import { AntDesignOutlined } from '@ant-design/icons';

ReactDOM.render(
  <Avatar
    size={{ xs: 24, sm: 32, md: 40, lg: 64, xl: 80, xxl: 100 }}
    icon={<AntDesignOutlined />}
  />,
  mountNode,
);