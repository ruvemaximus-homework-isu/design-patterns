from pydantic import BaseModel

from src.models.receipe import Receipe


class DataRepository(BaseModel):
    recipes: list[Receipe] = []
