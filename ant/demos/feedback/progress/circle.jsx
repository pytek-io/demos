import { Progress } from 'antd';

ReactDOM.render(
  <>
    <Progress type="circle" percent={75} />
    <Progress type="circle" percent={70} status="exception" />
    <Progress type="circle" percent={100} />
  </>,
  mountNode,
);