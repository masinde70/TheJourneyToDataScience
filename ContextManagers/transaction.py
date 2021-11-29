class Connection:
    """This connection class represents some sort of database connection.

    """
    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        print('start transaction', self.xid)
        rslt = self.xid
        self.xid = self.xid + 1
        return rslt

    def _commit_transaction(self, xid):
        print('committing transaction', xid)

    def _rollback_transaction(self, xid):
        print('rolling back transaction', xid)


class Transaction:
    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()


