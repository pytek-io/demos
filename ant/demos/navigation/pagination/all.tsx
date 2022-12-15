import { Pagination } from 'antd';

ReactDOM.render(
  <>
    <Pagination
      total={85}
      showSizeChanger
      showQuickJumper
      showTotal={total => `Total ${total} items`}
    />
  </>,
  mountNode,
);