from render_mantine.core import AppShell, Burger, MantineProvider, Center
from render_html import div
from render import ObservableValue

# import { useDisclosure } from '@mantine/hooks';


def app(_):
    test = ObservableValue(True)
    return MantineProvider(
        AppShell(
            [
                AppShell.Header(
                    [Burger(), "hello"],
                    # hiddenFrom="sm",
                    # size="sm",
                ),
                AppShell.Navbar("Navbar"),
                AppShell.Main(lambda: Burger(size=100) if test() else "hello"),
            ],
            header={"height": 60},
            navbar={
                "width": 800,
                "breakpoint": "sm",
                # collapsed: { mobile: !opened },
            },
            padding="md",
        )
    )
