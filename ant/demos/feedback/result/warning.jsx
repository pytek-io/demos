import { Result, Button } from 'antd';

ReactDOM.render(
  <Result
    status="warning"
    title="There are some problems with your operation."
    extra={
      <Button type="primary" key="console">
        Go Console
      </Button>
    }
  />,
  mountNode,
);