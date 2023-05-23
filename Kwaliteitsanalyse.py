import pandas as pd
from sqlalchemy import create_engine

# Database connection details
host = '81.206.183.249'
login = 'SA'
password = 'DEDSproject0!'
database = 'AenC'

# Create the database connection URL
connection_url = f'mssql+pymssql://{login}:{password}@{host}/{database}'

# Create the SQLAlchemy engine
engine = create_engine(connection_url)

# Query the database using pandas
table_name = 'dbo.bonus'
query = f'SELECT * FROM {table_name}'
df = pd.read_sql_query(query, engine)

# Print the retrieved data
print(df)