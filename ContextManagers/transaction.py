import contextlib


class Connection:
    """This connection class represents some sort of database connection.

    """
    def __init__(self):
        self.xid = 0

    @contextlib.contextmanager
    def start_transaction(connection):
        tx = Transaction(connection)

        try:
            yield tx
        except:
            tx.rollback()
            raise
        tx.commit()


    def _commit_transaction(self, xid):
        print('committing transaction', xid)

    def _rollback_transaction(self, xid):
        print('rolling back transaction', xid)


class Transaction:
    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.xid)

    def rollback(self):
        self.conn._rollback_transaction(self.xid)


