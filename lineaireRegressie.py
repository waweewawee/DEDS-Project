from statistics import LinearRegression
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder

# preset SQL server gegevens
server_name = '81.206.183.249'
database_name = 'DEDS'
username = 'SA'
password = 'DEDSproject0!'

# print drivers
print(pyodbc.drivers())

# verander "ODBC Driver *18* for SQL Server" naar v17 eventueel
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s;ENCRYPT=yes;' % (server_name, database_name, username, password)
con = pyodbc.connect(connection_string)

# Query uitvoeren en resultaten ophalen in een pandas dataframe
query = "SELECT Cost, Price FROM Product;"
df = pd.read_sql_query(query, con)

# Verbinding sluiten
con.close()

# Selecteren van de gewenste features (onafhankelijke variabelen) en de target (afhankelijke variabele)
X = df[['Cost']]  # Een enkele onafhankelijke variabele 'Cost'
y = df['Price']   # Afhankelijke variabele 'Price'

# Instantiëren van het lineaire regressiemodel
model = LinearRegression()

# Fit het model op de gegevens
model.fit(X, y)

# Krijg de geschatte coëfficiënten en intercept van het model
coef = model.coef_
intercept = model.intercept_

# Voer een voorspelling uit voor een bereik van waarden
X_pred = pd.DataFrame({'Cost': range(0, 100)})  # Bereik van kostwaarden voor voorspellingen
y_pred = model.predict(X_pred)

# Plot de gegevenspunten en de regressielijn
plt.scatter(X, y, color='black', label='Data')
plt.plot(X_pred, y_pred, color='blue', linewidth=3, label='Regression Line')
plt.xlabel('Cost')
plt.ylabel('Price')
plt.legend()
plt.show()







