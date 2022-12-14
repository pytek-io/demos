import { Avatar } from 'antd';

ReactDOM.render(
  <>
    <Avatar shape="circle" src="http://abc.com/not-exist.jpg">
      A
    </Avatar>
    <Avatar shape="circle" src="http://abc.com/not-exist.jpg">
      ABC
    </Avatar>
  </>,
  mountNode,
);