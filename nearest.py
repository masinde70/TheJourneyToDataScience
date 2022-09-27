def nearest_square(num):
    """Find the nearest square of a number.
    :param num:
    :return:
    """
    root = 0
    while (root + 1) ** 2 <= num:
        root += 1
    return root ** 2 
    