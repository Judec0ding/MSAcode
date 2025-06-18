"""
function to load menu item and price into a dictionary
Input: (string)file_path
Output: (dictionary)menu
"""  #str arrow dict is for user, not necessary
def get_menu_dictionary(file_name:str) -> dict:
    data_file = open("file.txt", "r")
    menu_items = {}
    for line_of_data in data_file:
        item_name_and_price = line_of_data.split(",")

        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])
        menu_items[item_name] = item_price

    data_file.close()
    return menu_items


def display_cart(cart:dict, menu_items:dict) ->None:
    print("\nCart\n----")
    total = 0
    #loop through the cart to print the output
    for item, quantity in cart.items():
        total = total + (quantity * menu_items[item])
        print(f"{quantity} {item} @{menu_items[item]:.2f}: {quantity * menu_items[item]}")
    print(f"\nTotal: ${total:.2f}")



def main():
    
    menu_items = get_menu_dictionary("file.txt")
    #create a cart dictionary
    cart_of_items = {}

    while True:
        item = input("\nItem: ")
        #determine if we need to end the program
        if item.lower() == "end":
            break

        #validate that item is in the menu_items dictionary
        if item not in menu_items: 
            print(f"\nERROR: {item} not on the menu")
            continue

        #prompt user for quantity
        try: 
            quantity = int(input("Quantity: "))
        except:
            print("\nERROR: enter number for quantity")
            continue
        

        #add item to cart. if item in cart already exists, add quantity 
        #if not in cart, add item and quantity to cart 
        if item not in cart_of_items:
            #create a new entry in the cart_of_items dictionary
            cart_of_items[item] = quantity
        else:
            #add quantity of item to existing quantity of item
            cart_of_items[item] += quantity

        #display total by calling the display_cart function
        display_cart(cart_of_items, menu_items)

        
        
        """
        2 Taco @3.00: 6.00
        3 Bowl @8.50: 25.50

        Total: $31.50
        """


        
main()