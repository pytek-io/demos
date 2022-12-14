import { message, Button } from 'antd';

const success = () => {
  message.success({
    content: 'This is a prompt message with custom className and style',
    className: 'custom-class',
    style: {
      marginTop: '20vh',
    },
  });
};

ReactDOM.render(<Button onClick={success}>Customized style</Button>, mountNode);