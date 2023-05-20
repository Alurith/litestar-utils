# litestar-utils

Utilities for the [Litestar framework](https://github.com/litestar-org/litestar).

**Source Code**: [https://github.com/Alurith/litestar-utils](https://github.com/Alurith/litestar-utils)

---
## Features: 
This package include some utilities I generaly use in my projects:
- **Timing Middleware**: Basic timing for each request
- **Slugify**: Basic slugify function with customizable options 

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

### Slugify:
Use the ```SlugifyOptions``` class to customize the behaviour.

```python

class SlugifyOptions(BaseModel):
    collapse_whitespace: bool = True
    disallowed_characters: str = r"[^\w\s-]"
    separator: str = "-"
    replacements: List = []
```

Simple example:
```python
from litestar_utils import slugify, SlugifyOptions

expected = "this-is-easy"
input_string = "this is easy"
assert slugify(input_string) == expected

```

Don't collaps whitespaces (default to ```True```):
```python
from litestar_utils import slugify, SlugifyOptions

expected = "should--not---collapse----whitespaces"
input_string = " should  not   collapse    whitespaces  "
options = SlugifyOptions(collapse_whitespace=False)
assert slugify(input_string, options=options) == expected

```

Custom separator (default to ```-```):
```python
from litestar_utils import slugify, SlugifyOptions

expected = "this.is.easy"
input_string = "this is easy"
options = SlugifyOptions(separator=".")
assert slugify(input_string, options=options) == expected
```

Replacements:
```python
from litestar_utils import slugify, SlugifyOptions

expected = "emailatexmapledotcom"
input_string = "email@exmaple.com"
options = SlugifyOptions(replacements=[("@", "at"), [".", "dot"]])
assert slugify(input_string, options=options) == expected

```
