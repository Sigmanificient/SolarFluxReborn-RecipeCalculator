from src.classes.counter import Counter


def recursive_list_count(collection, count_result=None):
    if count_result is None:
        count_result = Counter()

    if not len(collection):
        return Counter()

    for item in collection:
        if isinstance(item, list):
            recursive_list_count(item, count_result)

        else:
            count_result[item] += 1

    return count_result
