import { Button, message } from 'antd';

const key = 'updatable';

const openMessage = () => {
  message.loading({ content: 'Loading...', key });
  setTimeout(() => {
    message.success({ content: 'Loaded!', key, duration: 2 });
  }, 1000);
};

ReactDOM.render(
  <Button type="primary" onClick={openMessage}>
    Open the message box
  </Button>,
  mountNode,
);