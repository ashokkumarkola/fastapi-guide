# Server-Sent Events

Stream JSON Lines

text/event-stream format

What are Server-Sent Events?
SSE is a standard for streaming data from the server to the client over HTTP.

data: {"name": "Portal Gun", "price": 999.99}

data: {"name": "Plumbus", "price": 32.99}

from fastapi.sse import EventSourceResponse
from fastapi.sse import EventSourceResponse, ServerSentEvent

```
@app.get("/items/stream", response_class=EventSourceResponse)
    async def sse_items() -> AsyncIterable[Item]: # jsonable_encoder
        for item in items:
            yield item

@app.get("/items/stream-no-async", response_class=EventSourceResponse)
def sse_items_no_async() -> Iterable[Item]:
    for item in items:
        yield item


yield ServerSentEvent(data=item, event="item_update", id=str(i + 1), retry=5000)


```
