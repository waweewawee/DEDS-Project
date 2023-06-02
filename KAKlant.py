import pyodbc

server_name = 'LAPTOP-NQNF412J\\SQLEXPRESS'
database_name = 'DEDSproject'
connection_string = f'DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes;'

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

column_query = "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Klant'"
cursor.execute(column_query)
columns = cursor.fetchall()

null_count_queries = [f"SELECT COUNT(*) FROM Klant WHERE {column} IS NULL" for column, _ in columns]

for i, (column, data_type) in enumerate(columns):
    numeric_data_types = ['int', 'decimal', 'numeric', 'float', 'real', 'money', 'smallmoney']
    is_numeric = any(numeric_type in data_type.lower() for numeric_type in numeric_data_types)

    cursor.execute(null_count_queries[i])
    null_count = cursor.fetchone()[0]

    if is_numeric:
        number_count_query = f"SELECT COUNT(*) FROM Klant WHERE ISNUMERIC({column}) = 1 AND {column} IS NOT NULL"
        cursor.execute(number_count_query)
        number_count = cursor.fetchone()[0]
    else:
        number_count = 0

    letter_count_query = f"SELECT COUNT(*) FROM Klant WHERE {column} LIKE '%[A-Za-z]%' AND {column} IS NOT NULL"
    cursor.execute(letter_count_query)
    letter_count = cursor.fetchone()[0]

    print(f"Column: {column}, Null Count: {null_count}, Number Count: {number_count}, Letter Count: {letter_count}")

connection.close()