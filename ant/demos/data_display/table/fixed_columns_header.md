A Solution for displaying large amounts of data with long columns.

> Specify the width of columns if header and cell do not align properly. If specified width is not working or have gutter between columns, please try to leave one column at least without width to fit fluid layout, or make sure no [long word to break table layout](https://github.com/ant-design/ant-design/issues/13825#issuecomment-449889241).
>
> A fixed value which is greater than table width for `scroll.x` is recommended. The sum of unfixed columns should not greater than `scroll.x`.