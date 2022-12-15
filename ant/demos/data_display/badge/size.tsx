import { Badge } from 'antd';

ReactDOM.render(
  <>
    <Badge size="default" count={5}>
      <a href="#" className="head-example" />
    </Badge>
    <Badge size="small" count={5}>
      <a href="#" className="head-example" />
    </Badge>
  </>,
  mountNode,
);