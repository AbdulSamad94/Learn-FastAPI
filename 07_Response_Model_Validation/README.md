In **FastAPI**, `response_model` is used to control **what your API will return to the client**.

### 🔹 What is `response_model`?

It is an argument you use in your route functions to:

- **Filter the response data**
- **Validate the response**
- **Automatically document your API (in Swagger UI)**

---

### 🔹 Why use `response_model`?

1. ✅ To **hide sensitive data** (like passwords)
2. ✅ To **structure the response properly**
3. ✅ To **make your API clear and predictable**

---

### 🔹 Example:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str

@app.post("/create-user", response_model=UserOut)
def create_user(user: UserIn):
    return user  # Password will be hidden in the response
```

### 👇 What happens here?

- You send `username` and `password` in the request.
- FastAPI uses the `response_model=UserOut`, so it **only returns `username`**, and hides the `password`.

---

### 🔹 Summary:

- `response_model` = **output filter** using a Pydantic model.
- Helps keep your API secure, clean, and well-documented.
