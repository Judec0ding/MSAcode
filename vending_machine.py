def get_user_input(amount_due):
    #ask for user input that allows only 1, 5, 10, or 25
    #validate that user input is one of those integers by using a while loop
    #if user input invalid, reprompt question
    #return user input to 
    while True:
        try:
            coin_input = int(input("Enter coin: "))
            if (coin_input ==1) or (coin_input ==5) or (coin_input ==10) or (coin_input ==25):
                return coin_input
            else:
                print(f"Amount Due: {amount_due}")
                continue

        except:
            print(f"Amount Due: {amount_due}")

def do_calculations(amount_due, coin_input):
    #take user input and subtract it from 50
    #store amount due and pass it to main
    new_amount_due = amount_due - coin_input
    return new_amount_due

def main():
    #print vending machine, amount due, insert coin
    #create a while loop for getting user input 
    #user input function to get user input 
    #collect user input, pass it onto do_calculations
    #print amount due and rerun the loop
    #if amount due is below 0, break the loop
    amount_due = 50
    print("Vending Machine\n---------------")
    print(f"Amount Due: {amount_due}")
    while True:
        coin_input = get_user_input(amount_due)
        new_amount_due = do_calculations(amount_due, coin_input)
        amount_due = new_amount_due
        if new_amount_due <= 0:
            new_amount_due = new_amount_due * -1
            print(f"Change Owed: {new_amount_due}")
            break
        else:
            print(f"Amount due: {new_amount_due}")
            continue
        






main()