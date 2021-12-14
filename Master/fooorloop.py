def divisor():
    items = [2, 25, 9, 37, 28, 14]
    diivisor = 12

    for item in items:
        if item % diivisor == 0:
            found = item
            break
    else:  # nobreak
        items.append(diivisor)
        found = diivisor

    print("{items} contains {found} which is a multiple"
          f"of {diivisor}".format(**locals()))
