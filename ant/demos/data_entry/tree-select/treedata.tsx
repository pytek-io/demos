import { TreeSelect } from 'antd';

const treeData = [
  {
    title: 'Node1',
    value: '0-0',
    children: [
      {
        title: 'Child Node1',
        value: '0-0-1',
      },
      {
        title: 'Child Node2',
        value: '0-0-2',
      },
    ],
  },
  {
    title: 'Node2',
    value: '0-1',
  },
];

class Demo extends React.Component {
  state = {
    value: undefined,
  };

  onChange = value => {
    console.log(value);
    this.setState({ value });
  };

  render() {
    return (
      <TreeSelect
        style={{ width: '100%' }}
        value={this.state.value}
        dropdownStyle={{ maxHeight: 400, overflow: 'auto' }}
        treeData={treeData}
        placeholder="Please select"
        treeDefaultExpandAll
        onChange={this.onChange}
      />
    );
  }
}

ReactDOM.render(<Demo />, mountNode);