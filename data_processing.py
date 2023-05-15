import json
import pandas as pd
import numpy as np

def processing_name(item):
    return item.replace('\n    ','').replace('\n  ','')

def processing_category(category):
    return category.lower()

def processing_price(price):
    price = price.replace('\n          ','').replace('$','').replace('.','').split()[0]
    return int(price)
    
def processing_price_before(price_before):
    if price_before:
        price = price_before.replace('$','').replace('.','')
        return int(price)
    else:
        price = np.nan
        return price

def process_data(df_items):
    #Clean and process the data in these columns before further analysis or export. 
    # The `apply()` method is used to apply the specified function to each element of the column.
    df_items["Item name"] = df_items["Item name"].apply(processing_name)
    
    df_items["Category"] = df_items["Category"].apply(processing_category)
    
    df_items["Price"] = df_items["Price"].apply(processing_price)
    
    df_items["Price before"] = df_items["Price before"].apply(processing_price_before)
    
    return df_items

if __name__ == "__main__":
       
    data_json = r"E:\Practicas\webScraping_Project\items_tintas.json" 
    with open(data_json) as file:
        #Reading a JSON file located at the path and loading its contents into 
        items = json.load(file)    #a Python object called `items`

    # Creating a pandas DataFrame object called `df_items` from the JSON data stored 
    df_items = pd.DataFrame(items)
        
    df_items_end = process_data(df_items) #Calling the `process_data` function and passing the
    # `df_items` DataFrame as an argument. The function applies cleaning and processing
    # functions to specific columns using the `apply()` method.     

    data_csv = r"E:\Practicas\webScraping_Project\items_tintas_process.csv"    
    df_items_end.to_csv(data_csv, index=False)# Exporting the cleaned and processed data stored 
    #in the `df_items_end` DataFrame to a CSV file 