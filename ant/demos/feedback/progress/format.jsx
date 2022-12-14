import { Progress } from 'antd';

ReactDOM.render(
  <>
    <Progress type="circle" percent={75} format={percent => `${percent} Days`} />
    <Progress type="circle" percent={100} format={() => 'Done'} />
  </>,
  mountNode,
);