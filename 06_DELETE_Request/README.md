### 1. Purpose of DELETE

The `DELETE` method is used to remove a resource. In REST semantics, you target a specific item (usually by ID) and delete it. It should be idempotent, meaning calling it multiple times has the same end result (once deleted, further deletes usually return 404 or a no-op).

### 2. Basic FastAPI DELETE handler example

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# simple in-memory "database"
items = {
    1: {"name": "item one"},
    2: {"name": "item two"},
}

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    # delete the item
    del items[item_id]
    # 204 No Content means successful deletion with no body
    return
```

#### Explanation:

- `@app.delete("/items/{item_id}")`: defines a DELETE endpoint with a path parameter `item_id`.
- `status_code=status.HTTP_204_NO_CONTENT`: indicates success with no response body.
- If the item does not exist, we raise `HTTPException` with 404.
- If it exists, we remove it from the in-memory store.

### 3. Optional: Return a message instead of 204

If you prefer returning a JSON confirmation:

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()
items = {1: {"name": "item one"}, 2: {"name": "item two"}}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    del items[item_id]
    return {"message": f"Item {item_id} deleted successfully"}
```

This will return a 200 OK with a JSON message.

### 4. Idempotency note

If you call DELETE on the same `item_id` again after it's deleted:

- First call deletes and returns success.
- Subsequent calls usually return 404, which is acceptable and still considered idempotent in REST practice.

### 5. Advanced: Dependency and authorization (brief)

You can add dependencies like authentication or checks before deletion:

```python
from fastapi import Depends

def verify_user():
    # placeholder for auth logic
    pass

@app.delete("/items/{item_id}", dependencies=[Depends(verify_user)])
def delete_item(item_id: int):
    ...
```

### Summary

- Use `@app.delete(...)` with path param.
- Check if resource exists; if not, return 404.
- Delete and respond (204 no content or 200 with message).
- Optionally protect with dependencies.
