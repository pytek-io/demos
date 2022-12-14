import { Tag } from 'antd';
import { CloseCircleOutlined } from '@ant-design/icons';

ReactDOM.render(
  <>
    <Tag closable closeIcon="关 闭">
      Tag1
    </Tag>
    <Tag closable closeIcon={<CloseCircleOutlined />}>
      Tag2
    </Tag>
  </>,
  mountNode,
);