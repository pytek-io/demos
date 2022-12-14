import { Calendar } from 'antd';

function onPanelChange(value, mode) {
  console.log(value.format('YYYY-MM-DD'), mode);
}

ReactDOM.render(<Calendar onPanelChange={onPanelChange} />, mountNode);