
def main():
    
    #while True
    while True:
        #prompt the user for an expression
        user_expression = input("Expression: ")
        #use the split method to get the parts of the expression
        user_expression = user_expression.split(" ")
        #check the length of the list returned from .split
        #if len(list) not = 3, then output incorrect format message 
            #continue
        if len(user_expression) != 3:
            print("ERROR: Incorrect format. Please try again.") 
            continue
     
        #try:
        try:
            #get X and Y and Z values from the list
            x = user_expression[0]
            y = user_expression[1]
            z = user_expression[2]
            #and check if X and Z are integers by converting to int()
            x = int(x)
            z = int(z)
        #except:
        except:
            #output error message and reprompt
            print("ERROR: Incorrect format. X and Z must be integers. Please try again.")
            #continue
            continue
        #check that operator is +, -, *, /
        #if operator not in [+, -, *, /]:
        if y not in ["*", "/", "-", "+"]:
            #output error message
            print("ERROR: Incorrect format. Please try again.")
            #continue
            continue
        else:
            break
        
    #determine the operation to carry out based on the value of the operator
    #use if/elif/else block to evaluate operator and carry out the approved operation
    if y == "*":
        answer = x*z
        print(f"{x} {y} {z} = {answer:.1f}")
    elif y == "/":
        answer = x/z
        print(f"{x} {y} {z} = {answer:.1f}")
    elif y == "-":
        answer = x-z
        print(f"{x} {y} {z} = {answer:.1f}")
    else:
        answer = x+z
        print(f"{x} {y} {z} = {answer:.1f}")
    
    #output the answer



main()