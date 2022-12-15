import { Slider } from 'antd';

function formatter(value) {
  return `${value}%`;
}

ReactDOM.render(
  <>
    <Slider tipFormatter={formatter} />
    <Slider tipFormatter={null} />
  </>,
  mountNode,
);