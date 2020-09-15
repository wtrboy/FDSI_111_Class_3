def print_menu():
    print("--------------------------")
    print("Warehouse Mangement System")
    print("--------------------------")

    print('[1] Register New Item')
    print('[2] Display Catalog')
    print('[3] Items out of Stock')

    print('[7] Print the Stock Value')

    print('[x] Close')

def clear():
    print('\n\n\n\n')

def print_header(title):
    clear()
    print("----------------------------")
    print(title)
    print("----------------------------")