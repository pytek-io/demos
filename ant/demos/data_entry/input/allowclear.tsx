import { Input } from 'antd';

const { TextArea } = Input;

const onChange = e => {
  console.log(e);
};

ReactDOM.render(
  <>
    <Input placeholder="input with clear icon" allowClear onChange={onChange} />
    <br />
    <br />
    <TextArea placeholder="textarea with clear icon" allowClear onChange={onChange} />
  </>,
  mountNode,
);