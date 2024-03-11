import csv


def parse_csv(filename, select=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = []
        for row in rows:
            if not row:
                continue
            if select is False:
                record = dict({v: row[i] for i, v in enumerate(headers)})
            else:
                record = dict({
                    v: row[i] for i, v in enumerate(headers) if v in select})
            records.append(record)
    return records
