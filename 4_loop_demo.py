#This file will demonstrate how FOR LOOPS work

def main():
    #print integers between 0 and 10
    print("Output numbers between 0 and 10")
    for number in range(11):
        print(number)

    #print integers between 5 and 10
    print("\n\nOutput numbers between 5 and 10")
    for number in range(5,11):
        print(number)

    #print even numbers between 0 and 10
    print("\n\nOutput even numbers between 0 and 10")
    for number in range(0, 11, 2):
        print(number)

    #print odd numbers between 0 and 10
    print("\n\nOutput odd numbers between 0 and 10")
    for number in range(1, 11, 2):
        print(number)


    # prompt a user for the start and stop values and print the numbers between start and stop
    # get the start value from the user and convert to an integer
    # get the stop value from the user and convert to an integer
    # create a loop to run from start to stop
    start_value = int(input("Please enter a start value: "))
    end_value = int(input("Please enter a stop value: "))
    print(f"\n\nOutput numbers from {start_value} to {end_value}")
    for number in range (start_value, end_value + 1):
        print(number)


    # Use Nested for loops to print multiplication tables from user input
    # user will provide start and stop values for the tables
    start_value = int(input("Please enter a start table: "))
    end_value = int(input("Please enter a stop table: "))
    print(f"\n\nPrint multiplicaton tables from {start_value} to {end_value}")

    for table in range(start_value, end_value + 1):
        print(f"\nDisplaying the {table} multiplication table")
        for multiple in range(1, 13):
            product = table * multiple
            print(f"{table} x {multiple} = {product}")

main()