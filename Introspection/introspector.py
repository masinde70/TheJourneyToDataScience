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


def brief_doc(obj):
    doc = obj.__doc__
    if doc is not None:
        lines = doc.splitlines()
        if len(lines) > 0:
            return lines[0]
    return ''


def print_table(rows_of_columns, *headers):
    num_columns = len(rows_of_columns[0])
    num_headers = len(headers)
    if len(headers) != num_columns:
        raise TypeError("Expected {} header arguments, "
                        "got {}".format(num_columns, num_headers))
