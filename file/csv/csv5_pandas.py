import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)
df['Cost'] = df['Cost'].str.strip('$').astype(float)
df_value = df.loc[(df['Supplier']).str.contains('Z') | (df['Cost'] > 600.0), :]
df_value.to_csv(output_file, index=False)

