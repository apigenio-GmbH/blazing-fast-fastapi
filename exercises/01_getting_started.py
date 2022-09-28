from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Animal(BaseModel):
    # a name (str)
    # a description (str or None)
    # a height (float)
    # a weight (float or None)
    # abilities (list, 3.10 list of strings ;) )


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
    # return the animals


@app.put("/animals/{animal_id}")
async def update_animal(animal_id: int, animal: Animal):
    # append animals to list
    # print out result
    # return the result