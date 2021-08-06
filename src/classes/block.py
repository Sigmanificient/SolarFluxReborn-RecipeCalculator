from src.classes.item import Item


class Block(Item):

    def __init__(self, name: str, from_item: Item, amount: int = 9):
        super(Block, self).__init__(name, [from_item] * amount)
