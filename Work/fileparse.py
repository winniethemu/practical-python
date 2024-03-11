import csv


def parse_csv(
        filename,
        select=False,
        types=None,
        has_headers=True,
        delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
            headers = next(rows)
        records = []
        for row in rows:
            if not row:
                continue
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                if select is False:
                    record = dict({v: row[i] for i, v in enumerate(headers)})
                else:
                    record = dict({
                        v: row[i] for i, v in enumerate(headers) if v in select
                    })
            else:
                record = tuple(row)
            records.append(record)
    return records
