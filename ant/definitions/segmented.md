---
category: Components
group: Data Display
title: Segmented
cover: https://mdn.alipayobjects.com/huamei_7uahnr/afts/img/A*papwTpNscPIAAAAAAAAAAAAADrJ8AQ/original
demo:
  cols: 2
---

Segmented Controls. This component is available since `antd@4.20.0`.

## When To Use

- When displaying multiple options and user can select a single option;
- When switching the selected option, the content of the associated area changes.

## API

> This component is available since `antd@4.20.0`

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| block | Option to fit width to its parent\'s width | boolean | false |  |
| defaultValue | Default selected value | string \| number |  |  |
| disabled | Disable all segments | boolean | false |  |
| onChange | The callback function that is triggered when the state changes | function(value: string \| number) |  |  |
| options | Set children optional | string\[] \| number\[] \| Array<{ label: ReactNode value: string icon? ReactNode disabled?: boolean className?: string }> | [] |  |
| size | The size of the Segmented. | `large` \| `middle` \| `small` | - |  |
| value | Currently selected value | string \| number |  |  |