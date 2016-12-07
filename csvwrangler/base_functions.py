import csv


def extract_csv_column(file_handle, column=None, index=None):
    """
    extract a column from an opened csv file. Return an iterable.

    If neither value is specified, the first index will be returned.
    """
    if column is None and index is None:
        raise ValueError("either colname or index must be defined!")
    if column is None:
        return extract_csv_column_by_index(file_handle, index)
    else:
        return extract_csv_column_by_name(file_handle, column)


# the two functions below are inefficient, we should use generators
# to avoid reading everything to memory *but* this is a training example
# and generators are not part of basic curriculum
def extract_csv_column_by_name(file_handle, colname):
    reader = csv.DictReader(file_handle)
    return [float(item[colname]) for item in reader]


def extract_csv_column_by_index(file_handle, index):
    reader = csv.reader(file_handle)
    return [float(item[index]) for item in reader]
