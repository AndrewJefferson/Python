""" This program asks the user for their name and two numbers.
    It then adds and multiplies the numbers together
    and displays the results. """

# get input

# ask user for name
name = input("What is your name? ")

# ask user for two numbers
num_1 = int(input("What is your favourite number? "))
num_2 = int(input("What is your second favourite number? "))

# add numbers together
add = num_1 + num_2

# multiply numbers together
multiply = num_1 * num_2

# greet user and display math
print("Hello", name)

print(f"{num_1} + {num_2} = {add}")
print(f"{num_1} * {num_2} = {multiply}")