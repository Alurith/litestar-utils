# litestar-utils

Utilities for the [Litestar framework](https://github.com/litestar-org/litestar).

---
## Features: 
This package include some utilities I generaly use in my projects:
- **Timing Middleware**: Basic timing for each request 

---
## Installation: 
```sh
 $ pip install litestar-utils
```
or
```sh
 $ poetry add litestar-utils
```
---
## Usage: 

### Timing Middleware:
Use the `create_timing_middleware` function to create the middleware, the only required argument is `emit`.

`emit` must be a callable that accept 2 arguments a [Request](https://docs.litestar.dev/2/reference/connection.html#litestar.connection.Request) and a `float`


```python
from litestar import Litestar, get
from litestar_utils import create_timing_middleware


@get("/")
async def hello_world() -> str:
    return "Hello, world!"


@get("/base", exclude_timing=True)
async def base_all() -> str:
    return "All your base are belong to us"

app = Litestar(
    [hello_world, base_all],
    middleware=[create_timing_middleware(emit=print)],
)
```
