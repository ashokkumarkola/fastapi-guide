# PYDANTIC VALIDATION

## FIELD

```py
Field(
    default: ellipsis,
    *,
    alias: str | None = _Unset,
    alias_priority: int | None = _Unset,
    validation_alias: (
        str | AliasPath | AliasChoices | None
    ) = _Unset,
    serialization_alias: str | None = _Unset,
    title: str | None = _Unset,
    field_title_generator: (
        Callable[[str, FieldInfo], str] | None
    ) = _Unset,
    description: str | None = _Unset,
    examples: list[Any] | None = _Unset,
    exclude: bool | None = _Unset,
    exclude_if: Callable[[Any], bool] | None = _Unset,
    discriminator: str | Discriminator | None = _Unset,
    deprecated: Deprecated | str | bool | None = _Unset,
    json_schema_extra: (
        JsonDict | Callable[[JsonDict], None] | None
    ) = _Unset,
    frozen: bool | None = _Unset,
    validate_default: bool | None = _Unset,
    repr: bool = _Unset,
    init: bool | None = _Unset,
    init_var: bool | None = _Unset,
    kw_only: bool | None = _Unset,
    pattern: str | Pattern[str] | None = _Unset,
    strict: bool | None = _Unset,
    coerce_numbers_to_str: bool | None = _Unset,
    gt: SupportsGt | None = _Unset,
    ge: SupportsGe | None = _Unset,
    lt: SupportsLt | None = _Unset,
    le: SupportsLe | None = _Unset,
    multiple_of: float | None = _Unset,
    allow_inf_nan: bool | None = _Unset,
    max_digits: int | None = _Unset,
    decimal_places: int | None = _Unset,
    min_length: int | None = _Unset,
    max_length: int | None = _Unset,
    union_mode: Literal["smart", "left_to_right"] = _Unset,
    fail_fast: bool | None = _Unset,
    **extra: Unpack[_EmptyKwargs]
) -> Any
```
