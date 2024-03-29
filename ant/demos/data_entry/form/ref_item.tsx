import React from 'react';
import { Button, Form, Input } from 'antd';

const Demo = () => {
  const [form] = Form.useForm();
  const ref = React.useRef();

  return (
    <Form form={form} initialValues={{ list: ['light'] }}>
      <Form.Item name="test" label="test">
        <Input ref={ref} />
      </Form.Item>

      <Form.List name="list">
        {fields =>
          fields.map(field => (
            <Form.Item key={field.key} {...field}>
              <Input ref={ref} />
            </Form.Item>
          ))
        }
      </Form.List>

      <Button
        type="button"
        onClick={() => {
          form.getFieldInstance('test').focus();
        }}
      >
        Focus Form.Item
      </Button>
      <Button
        onClick={() => {
          form.getFieldInstance(['list', 0]).focus();
        }}
      >
        Focus Form.List
      </Button>
    </Form>
  );
};

ReactDOM.render(<Demo />, mountNode);