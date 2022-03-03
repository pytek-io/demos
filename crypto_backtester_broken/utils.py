import pandas as pd
import anyio


class PendingResult:
    def __init__(self) -> None:
        self.ready = anyio.Event()
        self.result = None
        self.is_error = True

    async def wait(self):
        await self.ready.wait()
        if self.is_error:
            raise Exception(self.result)
        return self.result

    def set(self, result, is_error):
        self.is_error = is_error
        self.result = result
        self.ready.set()


def to_timestamp(datetime):
    return int(datetime.timestamp()) * 1000


def from_timestamp(timestamp):
    return pd.to_datetime(timestamp / 1000, unit="s")


def bps(value):
    return value * 1000
