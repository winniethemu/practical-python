class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a plain-text table
    '''
    def headings(self, headers):
        for header in headers:
            print(f'{header:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for data in rowdata:
            print(f'{data:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for header in headers:
            print(f'<th>{header}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for data in rowdata:
            print(f'<td>{data}</td>', end='')
        print('</tr>')


def create_formatter(name):
    match name:
        case 'txt':
            return TextTableFormatter()
        case 'csv':
            return CSVTableFormatter()
        case 'html':
            return HTMLTableFormatter()
        case _:
            pass
