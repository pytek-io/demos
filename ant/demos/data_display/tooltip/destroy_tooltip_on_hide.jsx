import { Tooltip } from 'antd';

ReactDOM.render(
  <Tooltip destroyTooltipOnHide={{ keepParent: false }} title="prompt text">
    <span>Tooltip will destroy when hidden.</span>
  </Tooltip>,
  mountNode,
);