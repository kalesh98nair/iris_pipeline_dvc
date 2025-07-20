# src/transform.py
import sys
import pandas as pd

input_path = sys.argv[1]
output_path = sys.argv[2]

df = pd.read_csv(input_path)
df['sepal_area'] = df['sepal_length'] * df['sepal_width']
df.to_csv(output_path, index=False)
print(f"Transformed data saved to {output_path}")