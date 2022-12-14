import { Progress } from 'antd';

ReactDOM.render(
  <>
    <Progress type="dashboard" percent={75} />
    <Progress type="dashboard" percent={75} gapDegree={30} />
  </>,
  mountNode,
);