import { Descriptions, Divider } from 'antd';

const labelStyle: React.CSSProperties = { background: 'red' };
const contentStyle: React.CSSProperties = { background: 'green' };

function renderCelledDesc(bordered?: boolean) {
  return (
    <Descriptions title="User Info" bordered={bordered}>
      <Descriptions.Item label="Product" labelStyle={labelStyle} contentStyle={contentStyle}>
        Cloud Database
      </Descriptions.Item>
      <Descriptions.Item label="Billing Mode">Prepaid</Descriptions.Item>
      <Descriptions.Item label="Automatic Renewal">YES</Descriptions.Item>
    </Descriptions>
  );
}

function renderRootDesc(bordered?: boolean) {
  return (
    <Descriptions
      title="Root style"
      labelStyle={labelStyle}
      contentStyle={contentStyle}
      bordered={bordered}
    >
      <Descriptions.Item label="Product">Cloud Database</Descriptions.Item>
      <Descriptions.Item label="Billing Mode">Prepaid</Descriptions.Item>
      <Descriptions.Item
        label="Automatic Renewal"
        labelStyle={{ color: 'orange' }}
        contentStyle={{ color: 'blue' }}
      >
        YES
      </Descriptions.Item>
    </Descriptions>
  );
}

ReactDOM.render(
  <>
    {renderCelledDesc()}
    {renderCelledDesc(true)}

    <Divider />

    {renderRootDesc()}
    {renderRootDesc(true)}
  </>,
  mountNode,
);