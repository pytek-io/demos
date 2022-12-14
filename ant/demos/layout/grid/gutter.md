You can use the `gutter` property of `Row` as grid spacing, we recommend set it to `(16 + 8n) px` (`n` stands for natural number).

You can set it to a object like `{ xs: 8, sm: 16, md: 24, lg: 32 }` for responsive design.

You can use a array to set vertical spacing, `[horizontal, vertical]` `[16, { xs: 8, sm: 16, md: 24, lg: 32 }]`.

> vertical gutter was supported after `3.24.0`.