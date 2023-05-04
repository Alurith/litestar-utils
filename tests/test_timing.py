from unittest.mock import MagicMock

from litestar import get
from litestar.testing import create_test_client

from litestar_utils import create_timing_middleware


@get("/first_path")
async def first_path() -> str:
    return "Ok!"


@get("/second_path", exclude_timing=True)
async def second_path() -> str:
    return "Ok!"


@get("/third_path")
async def third_path() -> str:
    return "Ok!"


def test_path():
    emitter = MagicMock()
    with create_test_client(
        route_handlers=[first_path],
        middleware=[create_timing_middleware(emit=emitter)],
    ) as client:
        _response = client.get("/first_path")
        emitter.assert_called_once()


def test_exclude_one_path():
    emitter = MagicMock()
    with create_test_client(
        route_handlers=[first_path, third_path],
        middleware=[
            create_timing_middleware(
                emit=emitter,
                exclude="/first_path",
            )
        ],
    ) as client:
        _response = client.get("/first_path")
        emitter.assert_not_called()
        _response = client.get("/third_path")
        emitter.assert_called_once()


def test_exclude_multiple_paths():
    emitter = MagicMock()
    with create_test_client(
        route_handlers=[first_path, third_path],
        middleware=[
            create_timing_middleware(
                emit=emitter,
                exclude=["/first_path", "/third_path"],
            )
        ],
    ) as client:
        _response = client.get("/first_path")
        emitter.assert_not_called()
        _response = client.get("/third_path")
        emitter.assert_not_called()


def test_exclude_timing():
    emitter = MagicMock()
    with create_test_client(
        route_handlers=[first_path, second_path, third_path],
        middleware=[create_timing_middleware(emit=emitter)],
    ) as client:
        _response = client.get("/second_path")
        emitter.assert_not_called()
        _response = client.get("/first_path")
        emitter.assert_called_once()
        _response = client.get("/third_path")
        assert emitter.call_count == 2
