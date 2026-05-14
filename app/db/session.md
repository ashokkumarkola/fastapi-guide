## Lifecycle Flow

```
request starts
    ↓
create session
    ↓
API uses DB
    ↓
success → commit
failure → rollback
    ↓
close session
```

## Why Dependency Injection Matters

```
Without DI:
manual session management everywhere

With DI:
clean automatic lifecycle
```

## DO

```

use async sessions

use connection pooling

use request-scoped sessions

rollback failed transactions

centralize engine creation

```

## NEVER

```

create engine repeatedly

share global sessions

leave sessions unclosed

mix sync DB drivers with async engine

```
