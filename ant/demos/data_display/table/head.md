Use `filters` to generate filter menu in columns, `onFilter` to determine filtered result, and `filterMultiple` to indicate whether it's multiple or single selection.

Uses `defaultFilteredValue` to make a column filtered by default.

Use `sorter` to make a column sortable. `sorter` can be a function of the type `function(a, b) { ... }` for sorting data locally.

`sortDirections: ['ascend' | 'descend']` defines available sort methods for each columns, effective for all columns when set on table props. You can set as `['ascend', 'descend', 'ascend']` to prevent sorter back to default status.

Uses `defaultSortOrder` to make a column sorted by default.

If a `sortOrder` or `defaultSortOrder` is specified with the value `ascend` or `descend`, you can access this value from within the function passed to the `sorter` as explained above. Such a function can take the form: `function(a, b, sortOrder) { ... }`.