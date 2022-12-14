This demo shows how to use `Form.Item` with multiple controls. `<Form.Item name="field" />` will only bind the control(Input/Select) which is the only children of it. Imagine this case: you added some text description after the Input, then you have to wrap the Input by an extra `<Form.Item name="field">`. `style` property of `Form.Item` could be useful to modify the nested form item layout, or use `<Form.Item noStyle />` to turn it into a pure form-binded component(like `getFieldDecorator` in 3.x).


This demo shows three typical usages:

- `Username`: extra elements after control, using `<Form.Item name="field" noStyle />` inside `Form.Item` to bind Input.
- `Address`: two controls in one line, using two `<Form.Item name="field" noStyle />` to bind each control.
- `BirthDate`：two controls in one line with independent error message, using two `<Form.Item name="field" noStyle />` to bind each control, make layout inline by customizing `style` property.

> Note that, in this case, no more `name` property should be left in Form.Item with label.

See the `Customized Form Controls` demo below for more advanced usage.