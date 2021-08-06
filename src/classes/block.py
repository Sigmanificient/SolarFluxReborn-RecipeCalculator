from src.classes.item import Item


class Block(Item):

    def __init__(self, name, from_item, amount=9):
        super(Block, self).__init__(name, [from_item] * amount)
