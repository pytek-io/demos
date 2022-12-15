import { Result, Button } from 'antd';

ReactDOM.render(
  <Result
    status="500"
    title="500"
    subTitle="Sorry, something went wrong."
    extra={<Button type="primary">Back Home</Button>}
  />,
  mountNode,
);