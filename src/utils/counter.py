from typing import List, Any

from src.classes.counter import Counter


def recursive_list_count(collection: List[Any], count_result=None) -> Counter:
    if count_result is None:
        count_result: Counter = Counter()

    if not len(collection):
        return Counter()

    for item in collection:
        if isinstance(item, list):
            recursive_list_count(item, count_result)

        else:
            count_result[item] += item.per_craft

    return count_result
