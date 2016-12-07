from __future__ import print_function

import csv
import sys

def mean(iterable):
    return sum(iterable)/len(iterable)

def main():
    with open(sys.argv[1], "r") as f_:
        reader = csv.reader(f_)
        idx = int(sys.argv[2])
        datums = [float(x[idx]) for x in reader]
        print("mean is %s " % mean(datums))
if __name__ == "__main__":
    main()
