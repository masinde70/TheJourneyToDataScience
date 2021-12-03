import inspect


def dump(obj):
    print("Type")
    print("===")
    print(type(obj))
    print()

    print("Documentation")
    print("========")
    print(inspect.getdoc(obj))
    print()

    print("Attributes")
    print("==========")
    # TODO
    print()

    print("Methods")
    print("=======")
    # TODO
    print()


def full_sig(method):
    try:
        return method.__name__ + inspect.signature(method)
    except ValueError:
        return method.__name__ + '(...)'

