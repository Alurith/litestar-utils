from litestar import get
from litestar.testing import create_test_client

from litestar_utils import HTTPSRedirectMiddleware


@get("/")
async def root_path() -> str:
    return "Ok!"


def test_https_redirect():
    with create_test_client(
        route_handlers=[root_path],
        middleware=[HTTPSRedirectMiddleware],
    ) as client:
        assert client.base_url.scheme == "http"
        response = client.get("/")
        assert response.url.scheme == "https"
