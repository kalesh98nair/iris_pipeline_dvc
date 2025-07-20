import sys
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

csv_path = sys.argv[1]

username = 'postgres'
password = 'password'
host = 'localhost'
port = '5432'
database = 'iris-dvc'

df = pd.read_csv(csv_path)

connection_uri = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_uri)

df.to_sql('iris_data', con=engine, if_exists='replace', index=False)
print("✅ Data loaded into PostgreSQL successfully.")
