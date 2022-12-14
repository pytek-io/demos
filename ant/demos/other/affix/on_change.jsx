import { Affix, Button } from 'antd';

ReactDOM.render(
  <Affix offsetTop={120} onChange={affixed => console.log(affixed)}>
    <Button>120px to affix top</Button>
  </Affix>,
  mountNode,
);