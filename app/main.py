from fastapi import FastAPI

app = FastAPI()

from .routers import items, users

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/health")
def health():
    return {"status": "ok"}



