from litestar import Request, get
from litestar.status_codes import HTTP_200_OK
from litestar.testing import create_test_client

from litestar_utils import create_timing_middleware


@get("/first_path")
async def first_path() -> str:
    return "Ok!"


@get("/second_path", exclude_timing=True)
async def second_path() -> str:
    return "Ok!"


def emitter(request, timing):
    assert type(request) == Request
    assert type(timing) == float


def not_call_emitter(_request, _timing):
    assert True is False


def test_path():
    with create_test_client(
        route_handlers=[first_path],
        middleware=[create_timing_middleware(emit=emitter)],
    ) as client:
        response = client.get("/first_path")
        assert response.status_code == HTTP_200_OK
        assert response.text == "Ok!"


def test_exclude_root_path():
    with create_test_client(
        route_handlers=[first_path],
        middleware=[
            create_timing_middleware(
                emit=not_call_emitter,
                exclude=["first_path"],
            )
        ],
    ) as client:
        response = client.get("/first_path")
        assert response.status_code == HTTP_200_OK
        assert response.text == "Ok!"


def test_exclude_path():
    with create_test_client(
        route_handlers=[second_path],
        middleware=[create_timing_middleware(emit=not_call_emitter)],
    ) as client:
        response = client.get("/second_path")
        assert response.status_code == HTTP_200_OK
        assert response.text == "Ok!"
