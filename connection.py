import contextlib
import ssl
from itertools import count

import certifi
import websockets
from anyio import create_memory_object_stream
from msgpack import unpackb
from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK


class Connection:
    """handles serialization/deserialization, as well as providing a synchronous send API"""

    def __init__(self, connection, number_messages=True, dumps=None, loads=None):
        self.messages_sink, self.messages_stream = create_memory_object_stream(
            max_buffer_size=10000
        )
        self._connection = connection
        self.number_messages = number_messages
        self.dumps = dumps
        self.loads = loads or unpackb
        self.counter = count()

    async def close(self):
        await self._connection.close()

    async def recv(self):
        return self.loads(await self._connection.recv())

    async def __aiter__(self):
        try:
            while True:
                yield await self.recv()
        except ConnectionClosedError as exc:
            print(f"Connection closed with error: {exc}")
        except ConnectionClosedOK:
                pass

    async def send(self, message):
        try:
            await self._connection.send(self._serialize_message(message))
        except (ConnectionClosedError, ConnectionClosedOK):
            pass

    async def request_reply(self, message):
        await self.send(message)
        return await self.recv()

    def _serialize_message(self, message):
        if self.number_messages:
            message = next(self.counter), message
        if self.dumps:
            message = self.dumps(message)
        return message

    async def forward_to_connection(self):
        try:
            async for message in self.messages_stream:
                await self.send(message)
        except Exception:  # noqa: E722
            await self.close()

    def send_nowait(self, message):
        """Non blocking send (handy to avoid turning everything to async code)"""
        self.messages_sink.send_nowait(message)


def wrap_connection(
    connection, task_group=None, dumps=None, loads=None, number_messages=False
) -> Connection:
    connection = Connection(connection, number_messages, dumps=dumps, loads=loads)
    if task_group:
        task_group.start_soon(
            connection.forward_to_connection, name="forwarding messages"
        )
    return connection


@contextlib.asynccontextmanager
async def ws_connection_manager(
    uri, task_group=None, number_messages=False, dumps=None, loads=None
):
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(certifi.where())
    try:
        async with websockets.connect(uri, ssl=ssl_context) as connection:
            yield wrap_connection(
                connection=connection,
                task_group=task_group,
                number_messages=number_messages,
                dumps=dumps,
                loads=loads,
            )
    except Exception as exc:
        raise RuntimeError(
            f"Connection to {uri} terminated unexpectedly. {exc}"
        ) from exc
