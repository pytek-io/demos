import React, { useState } from 'react';
import { TimePicker } from 'antd';

const Demo = () => {
  const [value, setValue] = useState(null);

  const onChange = time => {
    setValue(time);
  };

  return <TimePicker value={value} onChange={onChange} />;
};

ReactDOM.render(<Demo />, mountNode);