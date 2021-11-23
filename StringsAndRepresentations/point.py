class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)

    def __format__(self, f):
        if f == 'r':
            return '{}, {}'.format(self.y, self.x)
        else:
            return '{}, {}'.format(self.x, self.y)


class Table:
    def __init__(self, header, *data):
        self.header = list(header)
        self.data = data
        assert len(header) == len(data)

    def _column_width(self, i):
        rslt = max(len(str(x)) for x in self.data[i])
        return max(len(self.header[i]), rslt)

    def __str__(self):
        col_count = len(self.header)
        col_widths = [self._column_width(i) for i in range(col_count)]
        format_specs = ['{{:{}}}'.format(col_widths[i])
                        for i in range(col_count)]

        rslt = []

        rslt.append(
            format_specs[i].format(self.header[i])
            for i in range(col_count))

        rslt.append(
            '=' * col_widths[i]
            for i in range(col_count))

        for row in zip(*self.data):
            rslt.append(
                [format_specs[i].format(row[i])
                 for i in range(col_count)])

        print(rslt)

        rslt = (' '.join(r) for r in rslt)

        return '\n'.join(rslt)
    
    def __repr__(self):
        return 'Table(header={}'.format(self.header)
