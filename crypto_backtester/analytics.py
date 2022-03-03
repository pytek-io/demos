import pandas as pd
from datetime import datetime

import py_vollib_vectorized
from py_vollib.black_scholes.implied_volatility import implied_volatility


def merge_data(instrument_data, currency_data):
    if not (instrument_data and instrument_data["ticks"]):
        return pd.DataFrame(
            {
                "volume_option": pd.Series(dtype="float64"),
                "ticks": pd.Series(dtype="<M8[ns]"),
                "close_option": pd.Series(dtype="float64"),
                "open_option": pd.Series(dtype="float64"),
                "close_spot": pd.Series(dtype="float64"),
            }
        )
    instrument_df = pd.DataFrame(
        dict(
            ticks=instrument_data["ticks"],
            **{
                f"{name}_option": instrument_data[name]
                for name in ["open", "close", "low", "high", "volume"]
            },
        )
    )
    currency_df = pd.DataFrame(
        {
            f"{name}_spot" if name != "ticks" else name: currency_data[name]
            for name in ["open", "close", "ticks"]
        }
    )
    result = pd.merge(
        currency_df[currency_df["ticks"] >= min(instrument_df["ticks"])],
        instrument_df,
        how="left",
        on=["ticks"],
    )
    result["ticks"] = [
        datetime.fromtimestamp(tick / 1000) for tick in instrument_df["ticks"]
    ]
    return result


def compute_implied_vols(df, strike, expiry, r, option_type):
    return implied_volatility(
        df["close_option"] * df["close_spot"],
        df["close_spot"],
        strike,
        df["ticks"].apply(lambda x: (expiry - x).days / 365),
        r,
        option_type,
        return_as="series",
    )


def compute_pnl(data, strike):
    daily_pnl_spot = np.zeros(len(data))
    daily_pnl_opt = np.zeros(len(data))
    capital = np.ones(len(data)) * capital_alloc
    pnl = np.zeros(len(data))
    for i in range(l, len(data)):
        price = data["close_option"][i]
        tick = data["ticks"][i]
        # Imply the volatility for the price on that date
        data["ivol_mid"][i] = iv(
            price, data["close_spot"][i], strike, (expiry - tick) / 365, r, flag
        )
        # And then use it to calculate the delta_mid on that date
        data["delta_mid"][i] = delta(
            flag,
            data["close_spot"][i],
            strike,
            (expiry - tick) / 365,
            r,
            data["ivol_mid"][i],
        )
        daily_pnl_opt[i] = (data["option"][i] - data["option"][i - 1]) * qty * mult
        daily_pnl_spot[i] = (
            (data["spot"][i] - data["spot"][i - 1])
            * data["delta_mid"][i - 1]
            * qty
            * mult
        )
        pnl[i] = pnl[i - 1] + daily_pnl_opt[i] - daily_pnl_spot[i] * is_delta_hedged
        capital[i] = capital[0] + pnl[i]


if __name__ == "__main__":
    instrument_name = "BTC-24JUN22-30000-C"
    import pickle

    df = pickle.loads(open(f"{instrument_name}.pick", "rb").read())
    _, expiry, strike, option_type = instrument_name.split("-")
    expiry, option_type = datetime.strptime(expiry, "%d%b%y"), option_type.lower()
    r = 0.01
    print(df.shape)
    print(compute_implied_vols(df, int(strike), expiry, r, option_type) * 100)
