import itertools
import reprlib
import inspect
from sorted_set import SortedSet


def dump(obj):
    print("Type")
    print("====")
    print(type(obj))
    print()

    print("Documentation")
    print("=============")
    print(obj.__doc__)
    print()

    all_attr_names = SortedSet(dir(obj))
    method_names = SortedSet(
        filter(lambda attr_name: callable(getattr(obj, attr_name)),
               all_attr_names))
    assert method_names <= all_attr_names
    attr_names = all_attr_names - method_names

    print("Attributes")
    print("==========")
    attr_names_and_values = [(name, reprlib.repr(getattr(obj, name)))
                             for name in attr_names]
    print_table(attr_names_and_values, "Name", "Value")
    print()

    print("Methods")
    print("=======")
    methods = (getattr(obj, method_name) for method_name in method_names)
    method_names_and_doc = [(full_sig(method), brief_doc(method)) for method in methods]
    print_table(method_names_and_doc, "Name", "Description")
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
