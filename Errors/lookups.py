def lookups():
    s = [1, 4, 6]
    try:
        item = s[5]
    except IndexError:
        print("Handled Index Error")
