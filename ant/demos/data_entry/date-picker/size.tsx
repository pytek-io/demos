import { DatePicker, Radio, Space } from 'antd';

const { RangePicker } = DatePicker;

class PickerSizesDemo extends React.Component {
  state = {
    size: 'default',
  };

  handleSizeChange = e => {
    this.setState({ size: e.target.value });
  };

  render() {
    const { size } = this.state;
    return (
      <Space direction="vertical" size={12}>
        <Radio.Group value={size} onChange={this.handleSizeChange}>
          <Radio.Button value="large">Large</Radio.Button>
          <Radio.Button value="default">Default</Radio.Button>
          <Radio.Button value="small">Small</Radio.Button>
        </Radio.Group>
        <DatePicker size={size} />
        <DatePicker size={size} picker="month" />
        <RangePicker size={size} />
        <DatePicker size={size} picker="week" />
      </Space>
    );
  }
}

ReactDOM.render(<PickerSizesDemo />, mountNode);