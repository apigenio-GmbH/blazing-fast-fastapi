from fastapi import FastAPI
application = FastAPI()

@application.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}