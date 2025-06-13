#function: to receieve season name
#input: (int)month number
#output: (string)month name
def get_season_name(month):
    if ((month ==1) or (month ==2) or (month ==12)):
         month = "winter"
    elif ((month ==3) or (month ==4) or (month ==5)):
         month = "spring"
    elif ((month ==6) or (month ==7) or (month ==8)):
         month = "summer"
    elif ((month ==9) or (month ==10) or (month ==11)):
         month = "fall"
    return month


#another way to write the same function for receving the season name:
def get_season_name_2(month: int):
    if month in [12, 1, 2]:
         month = "winter"
    elif month in [3, 4, 5]:
         month = "spring"
    elif month in [6, 7, 8]:
         month = "summer"
    elif month in [9, 10, 11]:
         month = "fall"
    return month

#function: to receieve month number
#input: answer from user
#output: (int)month number
def get_month_number():
    #validate the input is 1 - 12
    #reprompt user if input not valid
    while True:
        try:
            month_number = int(input("Please enter the month number: "))
            if ((month_number < 1) or (month_number > 12)):
                print("Please enter a valid month number from 1-12!")
                continue
            else:
                break
        except:
            print("ERROR: Please enter a number")
    return month_number


def main():
    #call the get_month_number function to prompt and get the month number from the user
    #call the get_season_name function to get the name of the season
    #print the output 
    #ask the user if they want to run the program again
    #if y or Y, rerun the program, otherwise end the program
    run_program_again = True
    while run_program_again:
        month_number = get_month_number()
        season_name = get_season_name(month_number)
        print(f"Month {month_number}/12 is in the {season_name} season.")
        run_again = input("Would you like to run the program again? Type 'y' to run again: ").lower()
        if run_again == "y":
            continue
        else:
            run_program_again = False




main()