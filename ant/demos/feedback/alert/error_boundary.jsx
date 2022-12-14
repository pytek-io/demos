import React, { useState } from 'react';
import { Button, Alert } from 'antd';

const { ErrorBoundary } = Alert;
const ThrowError: React.FC = () => {
  const [error, setError] = useState<Error>();
  const onClick = () => {
    setError(new Error('An Uncaught Error'));
  };

  if (error) {
    throw error;
  }
  return (
    <Button danger onClick={onClick}>
      Click me to throw a error
    </Button>
  );
};

ReactDOM.render(
  <ErrorBoundary>
    <ThrowError />
  </ErrorBoundary>,
  mountNode,
);