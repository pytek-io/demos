import io
import json
from datetime import datetime
from math import nan
from typing import List

import httpx
import pandas as pd

FRED_URL = "https://api.stlouisfed.org/fred/"
FRED_API_KEY = "84997d88a66df47cf034dce9c084157d"
YAHOO_URL = "https://query1.finance.yahoo.com/v7/finance/download/"


date_converter = lambda s: datetime.strptime(s, "%Y-%m-%d").date()
CONVERTERS = {
    "realtime_start": date_converter,
    "realtime_end": date_converter,
    "observation_start": date_converter,
    "observation_end": date_converter,
    "date": date_converter,
    "value": lambda s: float(s) if s != "." else nan,
}


def query_fred_website(path, data_name, **params):
    url = FRED_URL + "/".join(path)
    response = httpx.get(
        url,
        params=dict(api_key=FRED_API_KEY, file_type="json", **params),
    )
    if response.status_code != 200:
        raise Exception(
            f"Failed to retrieve data at {url}: {response.status_code}, {params}"
        )
    data = pd.DataFrame(json.loads(response.content.decode("UTF-8"))[data_name])
    for column_name in set(data.columns).intersection(CONVERTERS):
        data[column_name] = data[column_name].map(CONVERTERS[column_name])
    return data


def get_fred_series_observations(
    series_id: str, observation_start: datetime.date, observation_end: datetime.date
):
    return query_fred_website(
        ["series", "observations"],
        "observations",
        series_id=series_id,
        observation_start=observation_start.strftime("%Y-%m-%d"),
        observation_end=observation_end.strftime("%Y-%m-%d"),
    )


def get_fred_series_search(search_text: List[str]):
    return query_fred_website(
        ["series", "search"],
        "series",
        search_text="+".join(search_text),
    )


def get_fred_series_search(search_text: str):
    return query_fred_website(["series", "search"], "seriess", search_text=search_text)


def get_fred_series(series_id: str):
    return query_fred_website(["series"], "seriess", series_id=series_id)


def get_fred_category(category_id: int):
    return query_fred_website(["category"], "categories", category_id=category_id)


def get_fred_category_children(category_id: int):
    return query_fred_website(
        ["category", "children"], "categories", category_id=category_id
    )

def get_fred_category_series(category_id: int):
    return query_fred_website(
        ["category", "series"], "seriess", category_id=category_id
    )


def get_yahoo_stock_history(ticker, start, end):
    url = f"{YAHOO_URL}{ticker}?period1={int(start.timestamp())}&period2={int(end.timestamp())}&interval=1d&events=history"
    try:
        return pd.read_csv(io.BytesIO(httpx.get(url).content))
    except Exception as exception:
        raise RuntimeError(
            f"Failed to retrieve {ticker} data from yahoo: {exception}"
        ) from exception


if __name__ == "__main__":
    # df = get_fred_series_observations(
    #     "PCESVA",
    #     observation_start=datetime(2022, 6, 1).date(),
    #     observation_end=datetime(2022, 6, 1).date(),
    # )
    # import time

    # start = time.time()
    # results = []
    # for i in range(1, 4000):
    #     try:
    #         print(i)
    #         results.append(get_fred_category(i))
    #     except:
    #         print("failed")
    # print(time.time() - start)
    # pd.concat(results).to_pickle("categories.pick")
    print(get_fred_category_children(1))
    # df = get_fred_series_observations("T10Y20Y")
    # df = get_fred_series_search(["monetary", "service", "index"])
    # df.to_pickle("../fred.pick")
    # print(df)
    # r = get_fred_series_search("monetary+service+index")
