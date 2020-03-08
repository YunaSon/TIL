import sys
import pandas as pd

#input_file = sys.argv[1]
#output_file = sys.argv[2]

df = pd.read_csv('/Users/jooyoungson/TIL/file/csv/supplier_data.csv')
print(df)
df.to_csv('output_file', index=False)