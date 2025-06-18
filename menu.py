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

def main():
    
    menu_items = get_menu_dictionary("file.txt")
    total = 0
    
    while True:
        item = input("\nItem:\n ")
        if item.lower() == "end":
            break

        #get the item price from the dictionary
        try:
            item_price = menu_items[item]
        except:
            continue

        #add price to total
        total = total + item_price
        print(f"Total: ${total:.2f}")


        
main()