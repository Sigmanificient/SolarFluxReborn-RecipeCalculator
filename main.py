from typing import Optional, List, Dict, Counter

from src import cli, solar_panels
from src.classes.item import Item
from src.utils.counter import recursive_list_count


def main() -> None:
    action: Optional[str] = None

    while action != 'quit':
        tier: str = cli.choose_from('tier', *map(str, range(1, 7)))

        amount: str = ''
        while not amount.isdigit():
            amount = cli.ask('Choose an amount [1]') or '1'

        int_amount: int = int(amount)

        to_craft: List[Item] = (
            solar_panels[int(tier) - 1].get_raw_recipe() * int_amount
        )

        count: Counter = recursive_list_count(to_craft).round_up()

        cli.pretty_list(
            "Total ressources needed",
            (f"{k} x{v:,}" for k, v in sorted(count.items()))
        )

        action: str = cli.choose_from('action', 'get materials', 'quit')


if __name__ == '__main__':
    main()
