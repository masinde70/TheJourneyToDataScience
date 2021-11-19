def modulus_four(n):
    r = n % 4
    if r == 0:
        print("Multiple of 4")
    elif r == 1:
        print("reminder 1")
    elif r == 2:
        print("reminder 2")
    elif r == 3:
        print("reminder 3")
    else:
        assert False, "This should not happen"
