from __future__ import print_function
import sys

from base_functions import extract_csv_column
from statistics import mean

# argparse would be an excellent library for command line parsing and it would
# even make for a more compact intro but again, cognitive load is pretty
# awesome even without introducing yet another library


def main():
    if len(sys.argv) < 3:
        print("give at least two parameters: filename and colname or index")
        return
    fname = sys.argv[1]
    column = sys.argv[2]
    with open(fname, "r") as input_:
        if column.isdigit():
            value = mean(extract_csv_column(input_, index=int(column)))
        else:
            value = mean(extract_csv_column(input_, column=column))
        print("the mean is %s " % value)

if __name__ == "__main__":
    main()
