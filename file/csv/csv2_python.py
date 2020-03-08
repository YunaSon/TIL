import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as filereader:
    with open(output_file, 'w') as filewriter:
       for row in filereader:
            row = row.strip()
            print(row)
            wrow = row + '\n'
            filewriter.write(wrow)
    