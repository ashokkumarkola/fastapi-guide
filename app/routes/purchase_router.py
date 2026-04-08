from fastapi import APIRouter, BackgroundTasks
import time

router = APIRouter()


def log_purchase(user_id: int, item_id: int, order_id: int):
    # simulate slow logging
    time.sleep(2)

    with open("logs/purchases.txt", "a") as f:
        f.write(f"User {user_id} bought item {item_id} - Order Id {order_id} \n")


@router.post("/purchase")
def purchase(user_id: int, item_id: int, background_tasks: BackgroundTasks):
    
    # Core business logic (FAST)
    order_id = 123  # pretend DB save

    # Fire & forget logging
    background_tasks.add_task(log_purchase, user_id, item_id, order_id)

    return {
        "message": "Purchase successful",
        "order_id": order_id
    }