import { Pagination } from 'antd';

ReactDOM.render(
  <>
    <Pagination simple defaultCurrent={2} total={50} />
    <br />
    <Pagination disabled simple defaultCurrent={2} total={50} />
  </>,
  mountNode,
);