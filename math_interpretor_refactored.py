"""
Function to get valid expression inputs from the user
Input: None
Output: (int)X, (int)Y, (string)Y  
"""
def get_valid_expression_inputs():
    
    while True:
        user_expression = input("Expression: ")
        user_expression = user_expression.split(" ")
        if len(user_expression) != 3:
                print("ERROR: Incorrect format. Please try again.") 
                continue
        try:
            x = int(user_expression[0])
            z = int(user_expression[2])
            y = user_expression[1]
        except:
            print("ERROR: Incorrect format. X and Z must be integers. Please try again.")
            continue
        if y not in ["*", "/", "-", "+"]:
            continue
        elif (y == "/" and z == 0):
            print("ERROR: Cannot divide by 0. Please try again.")      
            continue
        else:
            break

    return x, y, z


"""
Function to evaluate an expression
Inputs: X(int), Y(string), Z(int)
Output: Answer from expression
"""
def evaluate_expression(x: int, y: str, z: int):
    
    if y == "*":
        answer = x*z
        return answer
    elif y == "+":
        answer = x/z
        return answer
    elif y == "-":
        answer = x-z
        return answer
    else:
        answer = x/z
        return answer

def main():
    while True:
        #call the get_valid_expression)inputs function to get x, y, z
        x, y, z = get_valid_expression_inputs()
        #call evaluate_Expression to get the answer for the expression
        answer = evaluate_expression(x, y, z)
        #print the answer
        print(f"{x} {y} {z} = {answer:.1f}")
        #ask the user if they want to evaluate another expression
        #rerun the program if the user wants to continue, otherwise end the program
        if input("Would you like to run another calculation? Type 'y' to run again if desired: ").lower() != "y":
            break
        else:
            continue

main()