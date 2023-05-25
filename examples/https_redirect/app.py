from litestar import Litestar, get

from litestar_utils import HTTPSRedirectMiddleware


@get("/")
async def hello_world() -> str:
    return "Hello, world!"


@get("/base", exclude_timing=True)
async def base_all() -> str:
    return "All your base are belong to us"


@get("/base/{some_id:int}")
async def base_world(some_id: int = 1) -> str:
    return f"base {some_id} belong to us"


app = Litestar(
    [hello_world, base_all, base_world],
    middleware=[HTTPSRedirectMiddleware],
)
