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

