from math import ceil

from src.classes.item import Item


class Counter(dict):

    def __getitem__(self, key: Item) -> int:
        if key not in self:
            self[key]: int = 0

        return super(Counter, self).__getitem__(key)

    def round_up(self):
        super(Counter, self).__init__({x: ceil(y) for (x, y) in self.items()})
        return self
