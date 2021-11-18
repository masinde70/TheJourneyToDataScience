import math


def inclination(dx, dy):
    """ The function returns the slope in degrees given the horizontal and vertical distance components

    """
    return math.degrees(math.atan(dx / dy))
