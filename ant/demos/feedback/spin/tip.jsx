import { Spin, Alert } from 'antd';

ReactDOM.render(
  <Spin tip="Loading...">
    <Alert
      message="Alert message title"
      description="Further details about the context of this alert."
      type="info"
    />
  </Spin>,
  mountNode,
);