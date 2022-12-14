import React, { useState } from 'react';
import { Space, Slider, Button } from 'antd';

function SpaceCustomizeSize() {
  const [size, setSize] = useState(8);

  return (
    <>
      <Slider value={size} onChange={value => setSize(value)} />
      <br />
      <br />
      <Space size={size}>
        <Button type="primary">Primary</Button>
        <Button>Default</Button>
        <Button type="dashed">Dashed</Button>
        <Button type="link">Link</Button>
      </Space>
    </>
  );
}

ReactDOM.render(<SpaceCustomizeSize />, mountNode);