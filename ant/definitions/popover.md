---
category: Components
type: Data Display
title: Popover
cover: https://gw.alipayobjects.com/zos/alicdn/1PNL1p_cO/Popover.svg
---

The floating card popped by clicking or hovering.

## When To Use

A simple popup menu to provide extra information or operations.

Comparing with `Tooltip`, besides information `Popover` card can also provide action elements like links and buttons.

## API

| Param   | Description         | Type                         | Default value | Version |
| ------- | ------------------- | ---------------------------- | ------------- | ------- |
| content | Content of the card | ReactNode \| () => ReactNode | -             |         |
| title   | Title of the card   | ReactNode \| () => ReactNode | -             |         |
| align | This value will be merged into placement's config, please refer to the settings [rc-tooltip](https://github.com/react-component/tooltip) | object | - |  |
| arrowPointAtCenter | Whether the arrow is pointed at the center of target | boolean | false |  |
| autoAdjustOverflow | Whether to adjust popup placement automatically when popup is off screen | boolean | true |  |
| color | The background color | string | - | 4.3.0 |
| defaultVisible | Whether the floating tooltip card is visible by default | boolean | false |  |
| destroyTooltipOnHide | Whether destroy tooltip when hidden, parent container of tooltip will be destroyed when `keepParent` is false | boolean \| { keepParent?: boolean } | false |  |
| getPopupContainer | The DOM container of the tip, the default behavior is to create a `div` element in `body` | function(triggerNode) | () => document.body |  |
| mouseEnterDelay | Delay in seconds, before tooltip is shown on mouse enter | number | 0.1 |  |
| mouseLeaveDelay | Delay in seconds, before tooltip is hidden on mouse leave | number | 0.1 |  |
| overlayClassName | Class name of the tooltip card | string | - |  |
| overlayStyle | Style of the tooltip card | object | - |  |
| placement | The position of the tooltip relative to the target, which can be one of `top` `left` `right` `bottom` `topLeft` `topRight` `bottomLeft` `bottomRight` `leftTop` `leftBottom` `rightTop` `rightBottom` | string | `top` |  |
| trigger | Tooltip trigger mode. Could be multiple by passing an array | `hover` \| `focus` \| `click` \| `contextMenu` \| Array&lt;string> | `hover` |  |
| visible | Whether the floating tooltip card is visible or not | boolean | false |  |
| onVisibleChange | Callback executed when visibility of the tooltip card is changed | (visible) => void | - |  |

Consult [Tooltip's documentation](/components/tooltip/#API) to find more APIs.

## Note

Please ensure that the child node of `Popover` accepts `onMouseEnter`, `onMouseLeave`, `onFocus`, `onClick` events.
