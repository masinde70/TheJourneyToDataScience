class LoggingContextManager:

    def __enter__(self):
        return "You're in a with-block!"

    def __exit__(self, exc_type, exc_val, exc_tb):
        return
