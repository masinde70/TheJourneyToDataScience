import inspect
import reprlib


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
    all_attr_names = SortedSet(dir(obj))
    method_names = SortedSet(filter(lambda attr_name:
                                    callable(getattr(obj, attr_name)),
                                    all_attr_names))
    print()

    print("Methods")
    print("=======")
    assert method_names <= all_attr_names
    attr_names = all_attr_names - method_names
    attr_names_and_values = [(name, reprlib.repr(getattr(object, name))) for name in all_attr_names]
    print_table(attr_names_and_values, "Name", "Value")
    methods = (getattr(obj, method_name) for method_name in method_names)
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

