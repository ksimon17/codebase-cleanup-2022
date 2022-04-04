
# READ INVENTORY OF PRODUCTS

#products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
#products_df = read_csv(products_filepath)
#products = products_df.to_dict("records")

import os

from app.utils import to_usd
from pandas import read_csv
import statistics

def filepath_compilation(csv_name):
    """
    This function takes in the nape of a CSV file name and compiles its appropriate filepath for the program. 
    Params: csv_name, which is the name of the csv file for which the function will retrieve its filepath
    Datatype of params: csv_name is of the String datatype 
    Return: this function returns the appropriate file_path of the csv file passed in to the function 

    Invoke this function like this: filepath_compilation("products.csv")
    """
    return os.path.join(os.path.dirname(__file__), "..", "data", csv_name)

def calculate_avg_price(prices):
    """
    This function accept any list or DataFrame of products as its input parameter, and returns the average price as a float (unformatted)
    Params: prices, which hold the prices of every individual product within the list or DataFrame of products passed in
    Datatype of params: prices is either of the List datatype or the Pandas DataFrame datatype
    Return: the average product price as an unformatted Float

    Invoke this function like this: calculate_avg_price(list_of_products)
    """
   # return statistics.mean(prices) 
    return statistics.median(prices) # is this incorrect?
    
if __name__ == "__main__":

    # checks to see if a products.csv file exists. If not, it uses the default
    if filepath_compilation("products.csv") == True:
        print("USING CUSTOM PRODUCTS CSV FILE...")
        csv_filepath = filepath_compilation("products.csv")
    else:
        print("USING DEFAULT PRODUCTS CSV FILE...")
        csv_filepath = filepath_compilation("default_products.csv")

    #reads the csv file into products variable
    products = read_csv(csv_filepath)
    #pandas transforms the data into a list of dictionaries
    products = products.to_dict('records')

    # PRINTED INVENTORY REPORT

    print("---------")
    print("THERE ARE", len(products), "PRODUCTS:")
    print("---------")

    # for p in products:
    #     print("..." + p["name"] + "   " + to_usd(p["price"]))

    # all_prices = []
    # for p in products:
    #     all_prices.append(float(p["price"]))

    all_prices = []
    for p in products: 
        print("..." + p["name"] + "   " + to_usd(p["price"]))
        all_prices.append(float(p["price"]))

   # avg_price = calculate_avg_price(all_prices)
    avg_price = statistics.median(all_prices) # is this the median price or the average price
    #avg_price = statistics.mean(all_prices)

    print("---------")
    print("AVERAGE PRICE:", to_usd(avg_price))

    # EMAIL INVENTORY REPORT