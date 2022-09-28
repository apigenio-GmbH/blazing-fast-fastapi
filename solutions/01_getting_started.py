from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Animal(BaseModel):
    name: str
    description: Union[str, None] = None
    height: float
    weight: Union[float, None] = None
    abilities: list = []


dog = Animal(
    name="Dog",
    description="This is a barking dog",
    height="0.5",
    weight=None,
    abilities=["friendly", "cute"]
)

cat = Animal(
    name="Cat",
    description="This is a small cat",
    height="0.2",
    weight=3.5,
    abilities=["fast", "cute", "small"]
)

animals = [dog, cat]


@app.get("/animals/{animal_id}")
async def get_animal(animal_id: int):
    return animals[animal_id]


@app.put("/animals/{animal_id}")
async def update_animal(animal_id: int, animal: Animal):
    animals.append(Animal(**animal.dict()))
    result = {"animal_id": animal_id, **animal.dict()}
    return result
