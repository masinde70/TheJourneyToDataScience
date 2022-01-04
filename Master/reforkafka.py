"""Kafka - the adventure game you can not win."""


def play():
    position = (0, 0)
    alive = True

    locations = {
        (0, 0): lambda: print("You are in maze of twisty passages, all alike."),
        (1, 0): lambda: print(" You are on a road in a dark forest. To the north you can see tower."),
        (1, 1): lambda: print("There is a tall tower here, with no obvious door. A path leads east.")

    }
    command = input()
    i, j = position
    if command == "N":
        position = (i, j + 1)
    elif command == "E":
        position = (i + 1, j)
    elif command == "S":
        position = (i, j - 1)
    elif command == "W":
        position = (i - 1, j)
    elif command == "L":
        pass
    elif command == "Q":
        position = None
    else:
        print("I don't understand")
        print("Game over")


if __name__ == '__main__':
    play()
