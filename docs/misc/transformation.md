# TRANSFORMATIONS

## JSON Compatible Encoder

- Pydantic model - JSON compatible version
- datetime objects - str

```py
from fastapi.encoders import jsonable_encoder

json_compatible_item_data = jsonable_encoder(item)
```

---

item.model_dump(exclude_unset=True)
