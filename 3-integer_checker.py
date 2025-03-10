# Ask user for number
# Loop question so that it repeats until valid number is entered
# Make code recyclable!

LOW = 1
HIGH = 15

valid = False
while not valid:
    num = input(f"Please enter an integer between {LOW} and {HIGH}: ")
    if num.lstrip('-').isnumeric():
        num = int(num)
        if num < LOW:
            print(f"{num} is lower than {LOW}")
        elif num > HIGH:
            print(f"{num} is greater then {HIGH}")
        else:
            valid = True
    else:
        print(f"{num} is not an integer")

print(f"Your number is {num}")