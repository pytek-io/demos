import { Checkbox } from 'antd';

function onChange(e) {
  console.log(`checked = ${e.target.checked}`);
}

ReactDOM.render(<Checkbox onChange={onChange}>Checkbox</Checkbox>, mountNode);