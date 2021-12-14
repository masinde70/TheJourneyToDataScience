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


def ensure_has_divisible(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
    items.append(divisor)
    return divisor


items = [2, 25, 9, 37, 24, 14]
divisor = 12

dividend = ensure_has_divisible(items, divisor)
print(f"{items} contains {dividend} which is a multiple of"
      "{divisor}".format(**locals()))