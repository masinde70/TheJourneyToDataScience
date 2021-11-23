import time


def make_timer():
    las_called = None  # Never

    def elapsed():
        nonlocal las_called
        now = time.time()
        if las_called is None:
            las_called = now
            return None
        result = now - las_called
        las_called = now
        return result
    return elapsed

