import pyodbc

server_name = 'LAPTOP-NQNF412J\\SQLEXPRESS'
database_name = 'DEDSproject'
connection_string = f'DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes;'

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()


update_klant_query = """
UPDATE Klant
SET
    KlantNaam = ISNULL(KlantNaam, 'onbekend'),
    KlantStad = ISNULL(KlantStad, 'onbekend'),
    KlantAdres = ISNULL(KlantAdres, 'onbekend'),
    KlantEmail = ISNULL(KlantEmail, 'onbekend'),
    KlantTelefoon = ISNULL(KlantTelefoon, 'onbekend'),
    Fax = ISNULL(Fax, 'onbekend'),
    KlantPostcode = ISNULL(KlantPostcode, 'onbekend'),
    KlantStaat = ISNULL(KlantStaat, 'onbekend')
WHERE
    KlantNaam IS NULL
    OR KlantStad IS NULL
    OR KlantAdres IS NULL
    OR KlantEmail IS NULL
    OR KlantTelefoon IS NULL
    OR Fax IS NULL
    OR KlantPostcode IS NULL
    OR KlantStaat IS NULL
"""

cursor.execute(update_klant_query)
connection.commit()

update_locatie_query = """
UPDATE Locatie
SET
    Regio = ISNULL(Regio, 'onbekend'),
    Stad = ISNULL(Stad, 'onbekend'),
    Adres = ISNULL(Adres, 'onbekend'),
    Postcode = ISNULL(Postcode, 'onbekend')
WHERE
    Regio IS NULL
    OR Stad IS NULL
    OR Adres IS NULL
    OR Postcode IS NULL
"""

cursor.execute(update_locatie_query)
connection.commit()

update_product_query = """
UPDATE Product
SET
    Type = ISNULL(Type, 'onbekend'),
    Quantity = ISNULL(Quantity, 'onbekend'),
    Color = ISNULL(Color, 'onbekend'),
    Description = ISNULL(Description, 'onbekend'),
    Size = ISNULL(Size, 'onbekend')
WHERE
    Type IS NULL
    OR Quantity IS NULL
    OR Color IS NULL
    OR Description IS NULL
    OR Size IS NULL
"""

cursor.execute(update_product_query)
connection.commit()

update_review_query = """
UPDATE Review
SET
    KlantID = ISNULL(KlantID, 'onbekend')
WHERE
    KlantID IS NULL
"""

cursor.execute(update_review_query)
connection.commit()

update_verkoop_query = """
UPDATE Verkoop
SET
    Aantal = ISNULL(Aantal, '-1')
WHERE
    Aantal IS NULL
"""

cursor.execute(update_verkoop_query)
connection.commit()

cursor.close()
connection.close()