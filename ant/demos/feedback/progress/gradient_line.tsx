import { Progress } from 'antd';

const Demo = () => (
  <>
    <Progress
      strokeColor={{
        '0%': '#108ee9',
        '100%': '#87d068',
      }}
      percent={99.9}
    />
    <Progress
      strokeColor={{
        from: '#108ee9',
        to: '#87d068',
      }}
      percent={99.9}
      status="active"
    />
    <Progress
      type="circle"
      strokeColor={{
        '0%': '#108ee9',
        '100%': '#87d068',
      }}
      percent={90}
    />
    <Progress
      type="circle"
      strokeColor={{
        '0%': '#108ee9',
        '100%': '#87d068',
      }}
      percent={100}
    />
  </>
);

ReactDOM.render(<Demo />, mountNode);