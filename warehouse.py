
"""
    Program: Warehouse Management System
     Author: M. Lane Thompson
      Func: 
            1 - Register Items
                - id (auto generated) (int)
                - title (str)
                - category (str)
                - stock (int)
                - price (float)
"""
# imports
from menu import print_menu, clear, print_header
from item import Item

# global variables
catalog = []

# functions
def register_item():
    try:
        print_header("Register Item")
        title = input('Please provide the Title: ')
        cat = input("Please provide the category: ")
        stock = int(input("Please provide initial stock: "))
        price = float(input("Please provide the price: "))

        item = Item(0, title, cat, stock, price)
        # add item to the catalog list
        catalog.append(item)

        print("** Item Saved! **")

    except ValueError:
        print("** Error, incorrect input, fix and try again")
    except:
        print('** Error, something went wrong! **')

def print_catalog():
    print_header("Items on Catalog")

    if(len(catalog) == 0):
        print("** Your catalog is empty ** \nUse option 1 to create items\n")
    else:
        for item in catalog:
            print(item.title)

def print_no_stock():
    for item in catalog:
        if(item.stock == 0):
            print(item.title)

# instructions 

opc = ''
while(opc !='x'):
    clear()
    print_menu()

    opc = input('Please select an option: ')
    if(opc == '1'):
            register_item()
    elif(opc == '2'):
            print_catalog()
    elif(opc == '3'):
            print_no_stock()
    input("Press Enter to continue")

print("Thank you, good bye!")