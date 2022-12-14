import { Select, Space } from 'antd';

interface ItemProps {
  label: string;
  value: string;
}

const options: ItemProps[] = [];

for (let i = 10; i < 36; i++) {
  const value = i.toString(36) + i;
  options.push({
    label: `Long Label: ${value}`,
    value,
  });
}

const Demo = () => {
  const [value, setValue] = React.useState(['a10', 'c12', 'h17', 'j19', 'k20']);

  const selectProps = {
    mode: 'multiple' as const,
    style: { width: '100%' },
    value,
    options,
    onChange: (newValue: string[]) => {
      setValue(newValue);
    },
    placeholder: 'Select Item...',
    maxTagCount: 'responsive' as const,
  };

  return (
    <Space direction="vertical" style={{ width: '100%' }}>
      <Select {...selectProps} />
      <Select {...selectProps} disabled />
    </Space>
  );
};

ReactDOM.render(<Demo />, mountNode);