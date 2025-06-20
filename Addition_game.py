import random

def get_level():
    #gets level from user
    #loop until input is valid
    while True:
        try:
            level = int(input("\nEnter level 1, 2, 3: "))
            if level <=3 and level >=1:
                break
            else:
                print("Invalid Input!")
                continue
        except:
            print("Invalid Input!")

    return level

def get_number_of_questions():
    #gets number of questions from the user
    #loops until input is valid
    while True:
        try:
            questions = int(input("\nEnter number of questions to ask: 3 to 10: "))
            if questions <=10 and questions >=3:
                break
            else:
                print("Please enter an integer value between 3 and 10!")
                continue
        except:
            print("Please enter an integer value between 3 and 10!")

    return questions

def main():

    #get user input from get_level function
    #call the get_level function
    level = get_level()
    #get user input for number of questions
    #call the get_number_of_questions function
    questions = get_number_of_questions()
    # create correct_answers variable to keep track of correct answers
    correct_answers = 0
    # create a random number generator variable (unnecessary)
    random_generator = random.Random()
    # set start and stop values for random number generator based on input level
    if level == 1:
        a = 0
        b = 9
    if level == 2:
        a = 10
        b = 99
    if level == 3:
        a = 100
        b = 999

    # for loop to generate random x and y values and prompt the user
    for question in range(questions):
        # generate random values for x and y based on 'a' and 'b' values
        x = random_generator.randint(a, b)  
        y = random_generator.randint(a, b)
        # keep track of sum to check if user input is correct later on
        sum = x + y
        # create another for loop to keep track of number of times a question is asked
        # for a variable, do it the number of times in range
        for prompt in range(3):
            #prompt user for answer to expression
            answer = input(f"\n{x} + {y} = ")
            #check that answer is correct
            if answer == str(sum):
                print("CORRECT!")
                #keep track of correct answers by + 1
                correct_answers += 1
                #move onto next question by breaking for loop
                break
            #otherwise
            else:
                print("INCORRECT!")
                # check if question has been asked 3 times, if prompt == 2 
                # if yes, print correct answer
                if prompt == 2:
                    print(f"\nCorrect Answer: {x} + {y} = {sum}")
    
    #calculate percantage of correct answers / questions by using variables, then multiply by 100
    percentage = (correct_answers/questions)*100
    #print final output statement
    print(f"\nYou got {correct_answers} out of {questions} questions correct: {percentage:.2f}%")






main()