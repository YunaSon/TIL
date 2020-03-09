from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
import sys
import glob
import os

inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, "r") as filereader:
        for row in filereader:
            print(row.strip())
