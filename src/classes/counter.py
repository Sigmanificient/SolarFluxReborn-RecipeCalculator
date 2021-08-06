from src.classes.item import Item


class Counter(dict):

    def __getitem__(self, key: Item) -> int:
        if key not in self:
            self[key]: int = 0

        return super(Counter, self).__getitem__(key)
