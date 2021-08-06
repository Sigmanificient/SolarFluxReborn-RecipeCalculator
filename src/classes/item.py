from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from src.classes.block import Block


@dataclass
class Item:
    name: str
    recipe: Optional[List[Union[Item, Block]]] = None
    per_craft: int = 1

    def __mul__(self, other):
        if other > 1:
            return [self] * other

        if not self.is_base:
            return [x for item in self.recipe for x in (item * other)]

        self.val = other
        return [self]

    def __iter__(self):
        return iter([self])

    def __add__(self, other):
        return [self] + list(other)

    def __radd__(self, other):
        return [self] + list(other)

    @property
    def is_base(self):
        return self.recipe is None
