import os
import psycopg2
import pandas as pd
import logging
# Setting the logging level to INFO.
logging.basicConfig(level=logging.INFO)

try:
    dbname = "tintas_products"
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")   
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connect = psycopg2.connect(
        database=dbname,
        host=host, 
        port=port,  
        user=user, 
        password=password
    )
    cursor = connect.cursor()
    # allows us to execute SQL commandson the connected database. 
    # The cursor object is used to interact 
    # with the database and execute SQL queries.
    
    data = r"E:\Practicas\webScraping_Project\items_tintas_process.csv"
    df = pd.read_csv(data)
    
    # This code is iterating over each row of a pandas DataFrame called `df` using the `iterrows()`
    # method. For each row, it is extracting the values of the columns "Item name", "Category",
    # "Price", and "Price before" and storing them in variables `name`, `category`, `price`, and
    # `price_before`, respectively.
    for index, row in df.iterrows():
        name = row["Item name"]
        category = row["Category"]
        price = row["Price"]
        price_before = row["Price before"]

        query = """INSERT INTO items (item_name, category, price, price_before)
        VALUES (%s, %s, %s, %s)"""
        values = (name, category, price, price_before)

        cursor.execute(query, values)
        
# Show the exception that may occur when connecting to the database using psycopg2 library. 
#it will log an error message with the specific error details using the logging module. 
except psycopg2.OperationalError as err:
        logging.error("Error connecting to the database: %s", err)
else:
    # Checking if the variable connect is in the local scope. If it is, it commits the changes.
    if 'connect' in locals() and 'cursor' in locals():
        connect.commit()  
        cursor.close()
        connect.close()
        
    # is logging an informational message indicating that the data has been successfully inserted 
    logging.info("Data inserted successfully.")