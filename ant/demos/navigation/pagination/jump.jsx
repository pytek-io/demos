import { Pagination } from 'antd';

function onChange(pageNumber) {
  console.log('Page: ', pageNumber);
}

ReactDOM.render(
  <>
    <Pagination showQuickJumper defaultCurrent={2} total={500} onChange={onChange} />
    <br />
    <Pagination showQuickJumper defaultCurrent={2} total={500} onChange={onChange} disabled />
  </>,
  mountNode,
);