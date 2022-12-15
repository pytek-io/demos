import { Upload, Button } from 'antd';
import { UploadOutlined } from '@ant-design/icons';

ReactDOM.render(
  <Upload action="https://www.mocky.io/v2/5cc8019d300000980a055e76" directory>
    <Button icon={<UploadOutlined />}>Upload Directory</Button>
  </Upload>,
  mountNode,
);