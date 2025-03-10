""" Online sandwich store - allows user to select options for their sandwich,
    calculates the total cost, and checks the order """

# Options for the fillings
breads = ["Wholemeal", "White", "Cheesy White", "Gluten Free"]
meats = []
garnish = []

# Prices for ingredients
prices = {
    "Wholemeal" : 1.00,
    "White" : 0.80,
    "Cheesy White" : 1.20,
    "Gluten Free" : 1.40,
    "None" : 0.00
}

# This is the ingredients of the sandwich the user is building
sandwich = {
    "Bread" : "None",
    "Meat" : "None",
    "Garnish" : "None"
}

def register_cost():
    """Keeps track of prices and adds this to the total cost"""
    temp = 0
    temp = temp + prices[sandwich["Bread"]] 
    temp = temp + prices[sandwich["Meat"]]   
    temp = temp + prices[sandwich["Garnish"]]  
    return round(temp * 100) / 100


def print_sandwich():
    """ Outputs the details about the sandwich the user has created """
    print("Bread = " + sandwich["Bread"] + " @ " + str(prices[sandwich["Bread"]]))
    print()
    print()


done = False
print("Welcome, ....dsfvlkjckovnhxov")
option = input("Type B to add Bread, M for Meat, G for Garnish")

while not done:
    if option.upper() == "B":
        print("Type the number next to the item you want to select")
        i = 1
        for item in breads:
            print(str(i) + ". " + item)
            i = i + 1
        temp = breads[int(input("")) - 1]
        sandwich["Bread"] = temp
    elif option.upper() == "M":

    elif option.upper() == "G":

    print("Here's your order so far")
    print_sandwich()
    print("Cost $" + str(register_cost()))

    option = "Type B to add Bread, M for Meat, G for Garnish, C to confrim your order"

    if option.upper() == "C":
        done = True

