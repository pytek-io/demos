import { Badge } from 'antd';

ReactDOM.render(
  <div>
    <Badge count={5} title="Custom hover text">
      <a href="#" className="head-example" />
    </Badge>
    <Badge count={-5} title="Negative">
      <a href="#" className="head-example" />
    </Badge>
  </div>,
  mountNode,
);