# FastAPI Composite Request Schema vs Multiple Body Parameters

When building APIs in FastAPI using a layered architecture (`router → service → DAO → schemas`), a common question appears when **one UI form submits multiple related entities**.

Example domain:

- Station
- StationSlots
- VideoConfig

Or another example:

- User
- Profile
- Settings

This document explains two approaches and when to use each.

---

# Approach 1 — Multiple Body Parameters

Example:

```python
@router.post("/stations")
def create_station(
    station: BroadcastStationCreate,
    slots: list[BroadcastStationSlotConfigCreate] | None = Body(default=None),
    config: VideoConfigCreate | None = Body(default=None),
):
    return service.create_station(station, slots, config)
```

Another example:

```python
@router.post("/users")
def create_user(
    user: UserCreate,
    profile: ProfileCreate,
    settings: UserSettingsCreate | None = None,
):
    return user_service.create_user(user, profile, settings)
```

---

## Advantages

- Less schema code
- Quick to implement
- Direct parameter mapping to service layer
- Works fine for small APIs

---

## Disadvantages

### 1. OpenAPI documentation becomes unclear

Swagger shows multiple request body sections instead of one object.

### 2. Hard to validate cross-entity logic

Example:

- profile requires user.email
- settings require profile.timezone

This validation becomes messy.

### 3. Harder to version APIs

Adding metadata later becomes difficult.

### 4. Response modeling becomes awkward

You still end up needing a combined response schema.

### 5. Not operation-centric

This approach models database entities instead of business actions.

---

## When this approach is acceptable

Use it when:

- Entities are independent
- No transactional logic
- Simple internal APIs
- Prototype code

---

# Approach 2 — Composite Request Schema (Recommended)

Create a schema representing the **business operation**.

---

## Station Example

```python
class BroadcastStationBundleCreate(BaseModel):
    station: BroadcastStationCreate
    slots: list[BroadcastStationSlotConfigCreate] | None = None
    config: VideoConfigCreate | None = None
```

Response:

```python
class BroadcastStationBundleResponse(BaseModel):
    station: BroadcastStationResponse
    slots: list[BroadcastStationSlotConfigResponse]
    config: VideoConfigResponse | None
```

Endpoint:

```python
@router.post("/stations", response_model=BroadcastStationBundleResponse)
def create_station(data: BroadcastStationBundleCreate):
    return station_service.create_full(data)
```

---

## User Example

```python
class UserBundleCreate(BaseModel):
    user: UserCreate
    profile: ProfileCreate
    settings: UserSettingsCreate | None = None
```

```python
class UserBundleResponse(BaseModel):
    user: UserResponse
    profile: ProfileResponse
    settings: UserSettingsResponse | None
```

```python
@router.post("/users", response_model=UserBundleResponse)
def create_user(data: UserBundleCreate):
    return user_service.create_full_user(data)
```

---

# Service Layer Pattern

Composite schemas work best with transactional services.

```python
def create_full_user(data: UserBundleCreate):
    user = user_dao.create(data.user)
    profile = profile_dao.create(user.id, data.profile)

    settings = None
    if data.settings:
        settings = settings_dao.create(user.id, data.settings)

    return {
        "user": user,
        "profile": profile,
        "settings": settings,
    }
```

---

# Advantages of Composite Schemas

## Clean API documentation

Single structured request body.

## Business-operation modeling

Represents what the API actually does.

## Easier validation

You can validate relationships inside one schema.

## Better transactions

Service layer can treat operation atomically.

## Easier versioning

New fields can be added without breaking endpoint signatures.

## Consistent response modeling

Request and response structures mirror each other.

## Scales well in large systems

Common in production APIs and microservices.

---

# Edge Cases to Consider

## Partial creation

If related entities are optional, mark them optional in bundle schema.

## Transactions

Always wrap DAO operations in a DB transaction.

## Nested validation

Use Pydantic validators for cross-entity checks.

## Updates vs Create

Composite schemas are more common for **create operations** than updates.

## Bulk operations

Composite schemas work well for bulk form submissions.

---

# Recommended Folder Structure

```
schemas/
    user.py
    profile.py
    settings.py
    user_bundle.py

services/
    user_service.py

dao/
    user_dao.py
```

---

# Rule of Thumb

Prefer **composite schemas** when:

- A single UI form submits multiple entities
- The operation is transactional
- Entities are related
- The API represents a business workflow

Use **multiple body parameters** only for simple or independent inputs.

---

# Final Recommendation

Composite request/response schemas are the **preferred production approach** in FastAPI applications using service-DAO architecture.
