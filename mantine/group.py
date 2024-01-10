from render_mantine import Button, Group


def app(_):
    return Group(
        [
            Button(1, variant="outline"),
            Button(2, variant="outline"),
            Button(3, variant="outline"),
        ],
        position="apart",
        grow=True,
    )
