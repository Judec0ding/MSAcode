# Print hello world
print("hello world!")

#create a variable to store my name
first_name = "Jude"

#print "My name is Jude"
print("My name is", first_name)

#create a variable to store my last name
last_name = "Thomas"

#write a statement to display "My full name is firstname lastname"
print("My full name is", first_name, last_name, sep="---")

# variables to store your age, height, weight, and assign them values
age = 16
height = 66
weight = 110.1

#print a sentence with age, weight, and height
print(f"My name is {first_name} {last_name}\nI am {age} years old and I weigh {weight}lbs")

#get and print the data type for age, weight, and height
print(type(age))
print(type(weight))
print(type(height))

#write 3 print statements using string interpolation (fstring) to print
#descriptive sentences for the data types
#Variable age is an int

print(f"Variable age is a {type(age)}")
print(f"Variable weight is a {type(weight)}")
print(f"Variable height is a {type(height)}")

number_1 = 2
number_2 = 6
total = number_1 + number_2
print(f"Total: {total}")

number_1 = "2"
number_2 = "6"
total = number_1 + number_2
print(f"Total: {total}")




