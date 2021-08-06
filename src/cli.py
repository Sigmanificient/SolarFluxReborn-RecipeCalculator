from PyInquirer import prompt


def choose_from(question, *choices):
    """Let the user choose between a list of options. return index."""
    return choices.index(
        prompt(
            {
                "type": "list",
                "name": "command",
                "message": question,
                "choices": choices
            }
        ).get("command")
    )


def ask(question):
    """Let the user enter a custom value."""
    return prompt(
        {
            'type': 'input',
            'name': 'replied',
            'message': question,
        }
    ).get("replied")
