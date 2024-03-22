import csv
import logging


log = logging.getLogger(__name__)


def parse_csv(
        lines,
        select=False,
        types=None,
        has_headers=True,
        delimiter=',',
        silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    if type(lines) is str:
        raise TypeError('expect file content instead of filename')

    rows = csv.reader(lines, delimiter=delimiter)
    if has_headers:
        headers = next(rows)
    records = []
    for index, row in enumerate(rows, 1):
        if not row:
            continue
        try:
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                if select is False:
                    record = dict({
                        v: row[i] for i, v in enumerate(headers)})
                else:
                    record = dict({
                        v: row[i] for i, v in enumerate(
                            headers) if v in select})
            else:
                record = tuple(row)
        except ValueError as e:
            if not silence_errors:
                log.warning(f'Row {index}: Couldn\'t convert {row}')
                log.debug(f'Row {index}: Reason {e}')
        records.append(record)
    return records
