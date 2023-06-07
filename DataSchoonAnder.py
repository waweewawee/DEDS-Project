import pyodbc
import pandas as pd

server_name = 'LAPTOP-NQNF412J\\SQLEXPRESS'
database_name = 'DEDSproject'
connection_string = f'DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes;'

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

def fill_null_with_most_common(column_name, table_name):
    query = f"SELECT TOP 1 {column_name} FROM {table_name} GROUP BY {column_name} ORDER BY COUNT(*) DESC"
    most_common_value = cursor.execute(query).fetchval()
    update_query = f"UPDATE {table_name} SET {column_name} = '{most_common_value}' WHERE {column_name} IS NULL"
    cursor.execute(update_query)
    connection.commit()

fill_null_with_most_common('KlantGender', 'Klant')
fill_null_with_most_common('KlantLeeftijd', 'Klant')
fill_null_with_most_common('Staat', 'Locatie')
fill_null_with_most_common('Cost', 'Product')
fill_null_with_most_common('SubCategory', 'Product')
fill_null_with_most_common('DateTime', 'Time')
fill_null_with_most_common('Year', 'Time')
fill_null_with_most_common('Quarter', 'Time')
fill_null_with_most_common('Month', 'Time')
fill_null_with_most_common('Week', 'Time')
fill_null_with_most_common('Day', 'Time')
fill_null_with_most_common('DayOfWeek', 'Time')
fill_null_with_most_common('DateTime', 'Time')

cursor.close()
connection.close()