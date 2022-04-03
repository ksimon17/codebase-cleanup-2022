


def to_usd(my_price):
    """
    This function formats a float variable such that it can be displayed in proper USD 
    currency formatting (i.e., 100.4 = $100.40). 
    Params: my_price, holds the the value of the number that needs to be formatted in to USD currency format
    Datatypes of params: my_price is a float datatype
    Return: this function will return the float variable passed in to the function in proper USD currency formatting 
    with two decimals.
    
    Invoke like this: to_usd(9.9999)

    """
    return '${:,.2f}'.format(my_price)


if __name__ == "__main__":
    
        
    # if this code is in the global scope
    # ... of a file we're trying to import from
    # ... it will throw errors when we try to run those other files
    price = input("Please choose a price like 4.9999")
    print(to_usd(float(price)))