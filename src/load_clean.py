# src/load_clean.py
import sys
import pandas as pd

input_path = sys.argv[1]
output_path = sys.argv[2]

df = pd.read_csv(input_path)
df.dropna(inplace=True)
df.to_csv(output_path, index=False)
print(f"Cleaned data saved to {output_path}")
