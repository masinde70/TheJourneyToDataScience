import contextlib
import sys


@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: enter')
    try:
        yield "You're in a with-block"
        print('logging_context_manager: normal exit')
    except Exception:
        print('logging_context_manager: exception exit',
              sys.exc_info())
        raise


@contextlib.contextmanager
def nest_test(name):
    print('Entering', name)
    yield name
    print('Exiting', name)


@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception:
        print(name, 'received an exception')
        if propagate:
            raise
