import math


class InclinationError(Exception):
    pass


def inclination(dx, dy):
    """ The function returns the slope in degrees given the horizontal and vertical distance components

    """
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope cannot be vertical") from e


def main():
    try:
        inclination(0, 5)
    except InclinationError as e:
        print(e.__traceback__)

if __name__ == '__main__':
    main()
    print("Finished")
