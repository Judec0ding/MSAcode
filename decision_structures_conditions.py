#This file demonstrates decision structures and conditions

def main():
    a = 6
    b = 7

    #exploring conditions
    print(f"a is greater than b: {a > b}")
    print(f"b is greater than a: {b > a}")
    print(f"a is equal to b: {a == b}")
    #comparison operators:
    #less than: <
    #greater than: >
    #less than or equal to: <=
    #greater than or equal to: >=
    #equal to: ==  (one equal sign is an assignment statement, two equal signs is a comparison operator)


    #create a decision structure to determine if a and b are equal
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print (f"{b} is greater than {a}")
    else:
        print(f"{a} is equal to {b}")


    #create a decision structure to print a letter grade based 
    #on a test score
    #A: 100-90, B: 89-80, C: 79-70, D: 69-60, F: <60

    print("Grade Decision: 1")
    test_score = 90

    #         A condition   and   B condition   (both must be true)
    if ((test_score <= 100) and (test_score >=90)):   
        print(f"{test_score} --> A")                
    elif ((test_score <=90) and (test_score >=80)):
         print(f"{test_score} --> B")
    elif ((test_score <=80) and (test_score >=70)):
         print(f"{test_score} --> C")
    elif ((test_score <=70) and (test_score >=60)):
         print(f"{test_score} --> D")
    else:
         print(f"{test_score} --> F")
main()