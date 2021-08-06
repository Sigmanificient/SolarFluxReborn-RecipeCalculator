from src.classes.block import Block
from src.classes.item import Item

import unittest

iron_ingot = Item('Iron Ingot')
iron_block = Block('Iron Block', iron_ingot)


class MyTestCase(unittest.TestCase):

    def test_base(self):
        self.assertFalse(iron_block.is_base)

    def test_recipes(self):
        self.assertEqual(
            iron_block.recipe,
            [iron_ingot] * 9
        )


if __name__ == '__main__':
    unittest.main()
