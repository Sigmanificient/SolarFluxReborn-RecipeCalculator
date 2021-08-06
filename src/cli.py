from PyInquirer import prompt


def choose_from(question, *choices):
    """Let the user choose between a list of options."""
    return prompt(
        {
            "type": "list",
            "name": "command",
            "message": question,
            "choices": choices
        }
    ).get("command")


def ask(question):
    """Let the user enter a custom value."""
    return prompt(
        {
            'type': 'input',
            'name': 'replied',
            'message': question,
        }
    ).get("replied")


def pretty_list(collection_name, collection):
    print('-' * 20)
    print(collection_name)
    print('\n'.join(f'- {item}' for item in collection))
    print('-' * 20)
