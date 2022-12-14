import { Progress } from 'antd';

ReactDOM.render(
  <>
    <Progress strokeLinecap="square" percent={75} />
    <Progress strokeLinecap="square" type="circle" percent={75} />
    <Progress strokeLinecap="square" type="dashboard" percent={75} />
  </>,
  mountNode,
);