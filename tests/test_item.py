from src.classes.item import Item

import unittest


stick = Item('Stick')
redstone = Item('Redstone')

redstone_torch = Item(
    'Redstone Torch',
    stick + redstone
)


class MyTestCase(unittest.TestCase):

    def test_base(self):

        self.assertTrue(stick.is_base)
        self.assertFalse(redstone_torch.is_base)

    def test_recipes(self):
        self.assertIsNone(stick.recipe)

        self.assertEqual(
            redstone_torch.recipe,
            [stick, redstone]
        )

    def test_operations(self):
        self.assertEqual(
            stick + redstone,
            [stick, redstone]
        )

        self.assertEqual(
            stick * 3,
            [stick] * 3
        )

        self.assertListEqual(
            stick * 2 + redstone,
            [redstone, stick, stick]
        )

        self.assertListEqual(
            redstone + stick * 2,
            [redstone, stick, stick]
        )


if __name__ == '__main__':
    unittest.main()
