import React, { useState, useEffect } from 'react';
import { Anchor } from 'antd';

const { Link } = Anchor;

const AnchorExample: React.FC = () => {
  const [targetOffset, setTargetOffset] = useState<number | undefined>(undefined);
  useEffect(() => {
    setTargetOffset(window.innerHeight / 2);
  }, []);
  return (
    <Anchor targetOffset={targetOffset}>
      <Link href="#components-anchor-demo-basic" title="Basic demo" />
      <Link href="#components-anchor-demo-static" title="Static demo" />
      <Link href="#API" title="API">
        <Link href="#Anchor-Props" title="Anchor Props" />
        <Link href="#Link-Props" title="Link Props" />
      </Link>
    </Anchor>
  );
};

ReactDOM.render(<AnchorExample />, mountNode);