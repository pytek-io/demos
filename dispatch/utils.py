import contextlib
import pickle
import time

import anyio


class ConnectionRecorder:
    def __init__(self, connection, archive):
        self.connection = connection
        self.archive = archive

        async def wrapper():
            previous_message = time.time()
            async for message in self.connection.messages:
                now = time.time()
                yield message
                self.archive.write(pickle.dumps([now - previous_message, message]))
                previous_message = now
                self.archive.flush()

        self.messages = wrapper()

    def recv(self):
        return self.messages

    async def send(self, message):
        return await self.connection.send(message)

    def send_nowait(self, message):
        self.connection.send_nowait(message)


def record_connection(connection, archive):
    return ConnectionRecorder(connection, archive)


class ReplayConnection:
    def __init__(self, archive):
        async def stream():
            for delay, message in archive:
                await anyio.sleep(delay)
                yield message

        self.messages = stream()

    def recv(self):
        return self.messages

    def __aiter__(self):
        return self.messages

    async def __anext__(self):
        return await self.messages.__anext__()

    async def send(self, _message):
        pass

    def send_nowait(self, _message):
        pass


def create_dummy_connection(archive):
    return ReplayConnection(archive)


@contextlib.asynccontextmanager
async def dummy_connection(archive):
    yield create_dummy_connection(archive)


def read_pickles(archive):
    try:
        while True:
            yield pickle.load(archive)
    except EOFError:
        pass


async def anext(async_generator):
    """async next version"""
    return await async_generator.__anext__()
