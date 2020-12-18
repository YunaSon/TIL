from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
import sys
import glob
import os

my_letters = ['a','b','c','d','e','f','g','h','i','j']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(max_index):
    if index_value < (max_index - 1):
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()