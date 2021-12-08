def is_comment(item):
    return isinstance(item, str) and item.startswith('#')


def execute(program):
    """ Execute a stack program.

    Args:
        program: Any stack-like collection where each item in the stack is
        callable operator or non-callable operand. The top-most items on the
        stack may be strings beginning with '#' for the purposes of documentation.
        Stack-like means supports for:

        item = stack.pop() # Remove and return the top item
        stack.append(item) # Push an item to the top
        if stack:          # False in boolean context when empty
    """
    # Find the start of the 'program' by skipping
    # any item which is a comment.
    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break

    else:  # no break
        print("Empty program")
        return

    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e:
                print("Error: ", e)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else:  # nobreak
        print("Program successful")
        print("Result: ", pending)
    print("Finished")
