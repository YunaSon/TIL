import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as filereader:
    with open(output_file, 'w') as filewriter:
        filereader = csv.reader(filereader, delimiter=',')
        filewriter = csv.writer(filewriter, delimiter=',')
        for row in filereader:
            print(row)
            filewriter.writerow(row)