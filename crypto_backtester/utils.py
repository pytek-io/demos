import pandas as pd


def to_timestamp(datetime):
    return int(datetime.timestamp()) * 1000


def from_timestamp(timestamp):
    return pd.to_datetime(timestamp / 1000, unit="s")


def bps(value):
    return value * 1000
