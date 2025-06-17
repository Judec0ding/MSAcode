def main():
    #open file.txt: create a file handler in read mode (default mode is read, but using 'r' to specify)

    #note: by defualt, opens the file in string, reads type of mode, and does that. In this case, 
    # it reads the file because of read mode, allowing for the for loop to go through each line in the file
    data_file = open("file.txt", "r")

    #create an empty dictionary to store "item: price" entries
    menu_items = {}

    #use a loop to read the contents of the file line by line 
    for line_of_data in data_file:
        #split the data at the comma
        item_name_and_price = line_of_data.split(",")

        #get the menu item and price from the list 
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        #create an entry in the dictionary for the item and price 
        #note: brackets add that value equal to another value, adding that as an entry into the dictionary
        menu_items[item_name] = item_price





main()