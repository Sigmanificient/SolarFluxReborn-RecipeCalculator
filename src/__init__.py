from src.classes.item import Item
from src.classes.block import Block

# Base materials

iron_ingot = Item('Iron Ingot')
glass = Item('Glass')
wooden_planks = Item('Wooden Planks')
cobblestone = Item('Cobblestone')
redstone = Item('Redstone')
lapis = Item('Lapis')
stick = Item('Stick')
gold = Item('Gold')
clay = Item('Clay')
glowstone_dust = Item('Glowstone Dust')
obsidian = Item('Obsidian')
diamond = Item('Diamond')
blaze_powder = Item('Blaze Powder')
quartz = Item('Quartz')

# Block
iron_block = Block('Iron block', iron_ingot)
gold_block = Block('Gold block', gold)
diamond_block = Block('Diamond block', diamond)
quartz_block = Block('Quartz block', quartz, amount=4)

# Solar panels components
redstone_torch = Item('Redstone torch', redstone + stick)
mirror = Item('Mirror', iron_ingot + glass * 3)
piston = Item('Piston', redstone + wooden_planks * 3 + cobblestone * 4)
repeater = Item('Repeater', redstone + cobblestone * 3 + redstone_torch * 2)
clock = Item('Clock', redstone + gold * 4)
redstone_lamp = Item('Redstone Lamp', glowstone_dust + redstone * 4)

# Photovoltaic cells
photovoltaic_cell_1 = Item(
    'Photovoltaic cell I',
    mirror + lapis * 3 + glass * 3
)

photovoltaic_cell_2 = Item(
    'Photovoltaic cell II',
    photovoltaic_cell_1 + (mirror * (2 / 3)) + lapis * 3 + clay * 3
)

photovoltaic_cell_3 = Item(
    'Photovoltaic cell III',
    photovoltaic_cell_2 + glowstone_dust * 3 + obsidian * 2 + glass * 3
)

photovoltaic_cell_4 = Item(
    'Photovoltaic cell IV',
    (
        photovoltaic_cell_3 + diamond + glowstone_dust * 2
        + blaze_powder * 3 + quartz_block * 2
    )
)

# Solar panels
solar_panel_1 = Item(
    "Solar Panel I",
    redstone + wooden_planks * 5 + mirror * 3
)

solar_panel_2 = Item(
    "Solar Panel II",
    piston + solar_panel_1 * 4
)

solar_panel_3 = Item(
    "Solar Panel III",
    iron_block + repeater + solar_panel_2 * 2 + photovoltaic_cell_1 * 3
)

solar_panel_4 = Item(
    "Solar Panel IV",
    iron_block + clock + solar_panel_3 * 2 + photovoltaic_cell_2 * 3
)

solar_panel_5 = Item(
    "Solar Panel V",
    (
        glowstone_dust + gold_block
        + solar_panel_4 * 2 + photovoltaic_cell_3 * 3
    )
)

solar_panel_6 = Item(
    "Solar Panel VI",
    (
        diamond_block + redstone_lamp
        + solar_panel_5 * 2 + photovoltaic_cell_4 * 3
    )
)

solar_panels = [
    solar_panel_1,
    solar_panel_2,
    solar_panel_3,
    solar_panel_4,
    solar_panel_5,
    solar_panel_6
]
