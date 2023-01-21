import datetime

import pandas as pd
import reflect as r
import reflect_altair as altair
import reflect_antd as antd
import reflect_html as html

from .charts import create_performance_chart
from .server import CURRENCIES, Server

TITLE = "Option backtester"


def create_cascading_selects(instruments):
    instruments = pd.DataFrame(instruments)
    select_style = {"width": 120, "paddingTop": 10}
    currency = antd.Select(
        options=[{"label": name, "value": acronym} for name, acronym in CURRENCIES],
        defaultValue=CURRENCIES[0][1],
        style=select_style,
    )

    def instrument_for_ccy():
        return instruments[instruments["base_currency"] == currency()]

    def expiry_timestamp_values():
        result = sorted(set(instrument_for_ccy()["expiration_timestamp"]), reverse=True)
        return result

    expiry_timestamp_select = antd.Select(
        options=lambda: [
            {
                "label": datetime.datetime.fromtimestamp(value / 1000).strftime(
                    "%d/%m/%y"
                ),
                "value": value,
            }
            for value in expiry_timestamp_values()
        ],
        defaultValue=expiry_timestamp_values()[2],
        style=select_style,
    )

    def reset_timestamp_value():
        if (
            expiry_timestamp_select()
            and expiry_timestamp_select() not in expiry_timestamp_values()
        ):
            expiry_timestamp_select.set(None)

    def instruments_for_expiry():
        return instrument_for_ccy()[
            instrument_for_ccy()["expiration_timestamp"] == expiry_timestamp_select()
        ]

    def option_types():
        return sorted(set(instruments_for_expiry()["option_type"]))

    option_type = antd.Select(
        options=lambda: [
            {"label": value[0].upper() + value[1:], "value": value}
            for value in option_types()
        ],
        style=select_style,
        defaultValue=option_types()[0] if option_types() else None,
    )

    def reset_option_type():
        if option_type() and option_type() not in option_types():
            option_type.set(None)

    def instruments_for_expiry_and_type():
        return instruments_for_expiry()[
            instruments_for_expiry()["option_type"] == option_type()
        ]

    def strikes():
        return sorted(set(instruments_for_expiry_and_type()["strike"]), reverse=True)

    strike = antd.Select(
        options=lambda: [
            {"label": f"{value:,.0f}", "value": value} for value in strikes()
        ],
        style=select_style,
        defaultValue=strikes()[min(len(strikes()) - 1, int(len(strikes()) / 2) + 1)]
        if strikes()
        else None,
    )

    def reset_strike():
        if strike() and strike() not in strikes():
            strike.set(None)

    def selected_instrument():
        if strike():
            selected_instruments = instruments_for_expiry_and_type()[
                instruments_for_expiry_and_type()["strike"] == strike()
            ]
            if selected_instruments.shape[0] != 1:
                print(
                    f"number of selection is different from one! {selected_instruments.shape[0]}"
                )
            return selected_instruments.iloc[0]["instrument_name"]

    r.autorun(reset_timestamp_value)
    r.autorun(reset_option_type)
    r.autorun(reset_strike)
    return (currency, expiry_timestamp_select, option_type, strike, selected_instrument)


class App(Server):
    async def async_init(self) -> None:
        instruments = await self.get_instruments()
        (
            currency,
            expiry_timestamp_select,
            option_type,
            strike,
            selected_instrument,
        ) = create_cascading_selects(instruments)
        chart_data = r.ObservableValue()

        async def update_chart_data():
            if selected_instrument():
                df, strike = await self.create_perf_chart_data(selected_instrument())
                self.window.update_title(selected_instrument())
                chart_data.set([df, strike])
            else:
                chart_data.set(None)

        def chart():
            data = chart_data()
            return html.div(
                altair.Chart(
                    create_performance_chart(*data),
                    style={"height": "42.5%", "width": "95%"},
                )
                if data
                else antd.Empty(description="Select an instrument"),
                style={"height": "100%", "flexGrow": 1},
            )

        r.autorun(update_chart_data)
        side_bar = antd.Col(
            [currency, expiry_timestamp_select, option_type, strike],
            style={"width": 200, "textAlign": "center"},
        )
        self.root = html.div(
            [chart, side_bar],
            style={
                "position": "absolute",
                "height": "100%",
                "width": "100%",
                "display": "flex",
                "flexFlow": "row",
                "paddingTop": 30,
                "paddingBottom": 30,
                "paddingRight": 10,
            },
        )


async def app(window: r.Window):
    app = App(window)
    await app.async_init()
    return app.root
