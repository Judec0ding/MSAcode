#Write a program that converts hourly wage and hours worked to a yearly salary
#A user will be prompted for their hours worked and their hourly wage
#The program will output the users hours worked, hourly wage, wages before taxes, tax amount, and annual wage after taxes

#GET INPUT FROM THE USER
#get user daily hours, ensure that it is positive and a number
def get_user_positive_floats():
    while True:
        try:
            user_daily_hours = float(input("Enter your daily hours worked: "))
            #ensure that daily hours are positive and above 0. If not, reprompt user
            if user_daily_hours <= 0 or user_daily_hours > 24:
                print("Error: Enter a value greater than 0 and less than 24")
                continue
            else:
                break
        except:
            print("ERROR: Please enter a number")

    return user_daily_hours

def get_user_hourly_wage():
    while True:
        try:
            user_hourly_wage = float(input("Enter your hourly wage: "))
            if user_hourly_wage <= 0:
                print("Error: Please enter a value greater than 0")
                continue
            else:
                break
        except:
            print("ERROR: Please enter a number")

    return user_hourly_wage
#PROCESSING
#Multiply hours worked in a day to hourly wage

def calculate_yearly_wage_without_taxes(hours, wage):
    daily_wage = hours * wage
    yearly_wage = daily_wage * 350
  
    return yearly_wage

def calculate_yearly_wage_with_taxes(yearly_wage):
    yearly_wage_with_taxes = yearly_wage * 0.88
   
    return yearly_wage_with_taxes


def main ():
    user_daily_hours = get_user_positive_floats()
    user_hourly_wage = get_user_hourly_wage()
    yearly_wage = calculate_yearly_wage_without_taxes(user_daily_hours, user_hourly_wage)
    yearly_wage_with_taxes = calculate_yearly_wage_with_taxes(yearly_wage)
    tax_amount = yearly_wage - yearly_wage_with_taxes

    print("Pay Advice")
    print("----------")
    print(f"Hours Worked: {user_daily_hours:.2f}")
    print(f"Hourly Wage: ${user_hourly_wage:.2f}")
    print(f"Wages Before Taxes: ${yearly_wage:.2f}")
    print(f"Tax Amount: ${tax_amount:.2f}")
    print(f"Annual Wage After Taxes: ${yearly_wage_with_taxes:.2f}")

main()