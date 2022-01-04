"""Kafka - the adventure game you can not win."""


def play():
    position = (0, 0)
    alive = True

    locations = {
        (0, 0): labyrinth,
        (1, 0): dark_forest_road,
        (1, 1): tall_tower,
        (2, 1): rabbit_hole,
        (1, 2): lava_pit,

    }
    try:
        location_action = locations[position]
    except KeyError:
        print("There is nothing here.")
    else:
        position, alive = location_action(position, alive)

    actions = {
        'N': go_north,
        'E': go_east,
        'S': go_south,
        'W': go_west,
        'L': look,
        'Q': quit,
    }

    try:
        command_action = actions[position]()
    except KeyError:
        print("I don't understand.")
    else:
        position = command_action(position)


def labyrinth(position, alive):
    print("You are in maze of twisty passages, all alike.")
    return position, alive


def dark_forest_road(position, alive):
    print(" You are on a road in a dark forest. To the north you can see tower.")
    return position, alive


def tall_tower(position, alive):
    print("There is a tall tower here, with no obvious door. A path leads east.")
    return position, alive


def rabbit_hole(position, alive):
    print("You fall down a rabbit hole into a labyrinth.")
    return (0, 0), alive


def lava_pit(position, alive):
    print("You fall into a lava pit.")
    return position, False


def go_north(position):
    i, j = position
    new_position = (i, j + 1)
    return new_position


def go_east(position):
    i, j = position
    new_position = (i + 1, j)
    return new_position


def go_south(position):
    i, j = position
    new_position = (i, j - 1)
    return new_position


def go_west(position):
    i, j = position
    new_position = (i - 1, j)
    return new_position


def look(position):
    return position


def quit(position):
    return None


if __name__ == '__main__':
    play()
