from bs4 import BeautifulSoup
import requests
import json

def get_html_info(base_url, pages_site):
    
    items = []    
    for n in range(1, pages_site): 
        # Creating a new url for each page. 
        url = f"{base_url}page={n}" 
        # is a formatted string literal in Python. 
                
        page = requests.get(url)
        # is making a GET request to the URL specified by the `url` variable
        
        soup = BeautifulSoup(page.text, 'html.parser')
        # `page.text` attribute contains the HTML content of the web
        # `'html.parser'` is the parser used to parse the HTML content. 
        
        items_found = soup.find_all('div', class_='infor')

        items.extend(items_found) #it adds multiple elements
        
    return items

def get_info_items(item):
    
    info_items = {}
    info_items["Item name"] = item.find('a', class_='title').text
    info_items["Category"] = item.find('div', class_='category').text  
    info_items["Price"] = item.find('div', class_='price').text
    info_items["Price before"] = item.find('del', class_='d-inline-block')
    info_items["Price before"] = info_items["Price before"].text if info_items["Price before"] else ""
       
    return info_items
     
# Run the main function only when you want to run the module as a program
if __name__ == "__main__":
    
    BASE_URL = 'https://todotintasysuministros.com/celulares-y-tablets?'    
    
    page_site = 4 #Range page number enabled in site
    
    items = get_html_info(BASE_URL,page_site)# it is calling the `get_html_info` function with the
    # `BASE_URL` and `page_site` arguments, and assigning the returned value to the `items` variable.

    list_info_items = []    
    for item in items:
        info_items = get_info_items(item) #Calling function and extract specific information from the item and add it in dictionary `info_items`.
        list_info_items.append(info_items) #The dictionary is appended to the `list_info_items` list.
    
    data_json = r"E:\Practicas\webScraping_Project\items_tintas.json" 
    
    with open(data_json, "w") as outfile:  #The `with open(data_json, "w") as outfile:` statement is
    # used to open the file in write mode (`"w"`) and assign it to the `outfile` variable.
        json.dump(list_info_items, outfile, indent=4) 
        #This creates a JSON file containing the extracted information from the web page.

