from src import cli, solar_panels


def main():
    action = None

    while action != 'quit':
        tier = cli.choose_from('tier', *map(str, range(1, 7)))
        print(solar_panels[int(tier) - 1])

        action = cli.choose_from('action', 'get materials', 'quit')


if __name__ == '__main__':
    main()
