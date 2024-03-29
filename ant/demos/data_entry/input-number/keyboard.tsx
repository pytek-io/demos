import { InputNumber, Button } from 'antd';

class App extends React.Component {
  state = {
    keyboard: true,
  };

  toggle = () => {
    this.setState({
      keyboard: !this.state.keyboard,
    });
  };

  render() {
    return (
      <>
        <InputNumber min={1} max={10} keyboard={this.state.keyboard} defaultValue={3} />
        <div style={{ marginTop: 20 }}>
          <Button onClick={this.toggle} type="primary">
            Toggle keyboard
          </Button>
        </div>
      </>
    );
  }
}

ReactDOM.render(<App />, mountNode);