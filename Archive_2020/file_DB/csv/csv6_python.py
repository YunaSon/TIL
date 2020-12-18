import csv
import sys

# if sys.argv[1]:
#     input_file = sys.argv[1]
# else:
input_file = 'supplier_data1.csv'

# if sys.argv[2]:
# output_file = sys.argv[2]
# else:
output_file = 'output6'

with open(input_file, 'r') as filereader:
    with open(output_file, 'w') as filewriter:
        filereader = csv.reader(filereader)
        filewriter = csv.writer(filewriter)
        header = next(filereader)
        for row in filereader:
            supplier = str(row[0]).strip()
            cost = str(row[3]).strip('$').replace(',','')
            if supplier == 'SupplierZ' or float(cost) > 600:
                print(row)
                filewriter.writerow(row)
