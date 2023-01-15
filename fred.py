import httpx
import json
import pandas as pd
from datetime import datetime
from math import nan

series_id = "SP500"
root_url = "https://api.stlouisfed.org/fred/"
api_key = "84997d88a66df47cf034dce9c084157d"
url = root_url + "/series/observations"
url = root_url + "/series/search"


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
    url = root_url + "/".join(path)
    response = httpx.get(
        url,
        params=dict(
            api_key="84997d88a66df47cf034dce9c084157d", file_type="json", **params
        ),
    )
    if response.status_code != 200:
        raise Exception(
            f"Failed to retrieve data at {url}: {response.status_code}, {params}"
        )
    data = pd.DataFrame(json.loads(response.content.decode("UTF-8"))[data_name])
    for column_name in set(data.columns):
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


def get_fred_series_search(search_text: str):
    return query_fred_website(["series", "search"], "seriess", search_text=search_text)


if __name__ == "__main__":
    # df = get_fred_series_observations("SP500")
    df = get_fred_series_observations("T10Y20Y")
    print(df)
    # r = get_fred_series_search("monetary+service+index")
