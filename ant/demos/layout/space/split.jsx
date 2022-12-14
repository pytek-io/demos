import { Space, Typography, Divider } from 'antd';

function SpaceSplit() {
  return (
    <Space split={<Divider type="vertical" />}>
      <Typography.Link>Link</Typography.Link>
      <Typography.Link>Link</Typography.Link>
      <Typography.Link>Link</Typography.Link>
    </Space>
  );
}

ReactDOM.render(<SpaceSplit />, mountNode);