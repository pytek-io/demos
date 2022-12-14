import { Switch, Button } from 'antd';

const App = () => {
  const [disabled, setDisabled] = React.useState(true);

  const toggle = () => {
    setDisabled(!disabled);
  };

  return (
    <>
      <Switch disabled={disabled} defaultChecked />
      <br />
      <Button type="primary" onClick={toggle}>
        Toggle disabled
      </Button>
    </>
  );
};

ReactDOM.render(<App />, mountNode);