# Starter Code for Building REST APIs with FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# TODO: Define the Item Pydantic model with 'name' (str) and optional 'description' (str)
# class Item(BaseModel):
#     ...

# In-memory storage for items
items = []

# TODO: Define a GET / route that returns a welcome message
# @app.get("/")
# def root():
#     ...

# TODO: Define a GET /items route that returns all items
# @app.get("/items")
# def get_items():
#     ...

# TODO: Define a POST /items route that accepts an Item body and appends it to the list
# @app.post("/items")
# def create_item(item: Item):
#     ...

# TODO: Define a DELETE /items/{item_id} route that removes an item by index
#       Raise HTTPException with status_code=404 if the item_id is out of range
# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     ...
