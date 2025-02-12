from random import choice
drinks = ["gin", "vodka", "whiskey", "rum", "tequila", "absinthe", "sake", "beer", "wine"] # list uses square brackets
# print(choice(drinks))
name = input("I am the virtual bartender. What is your name? ")
legal = False
beer_country = ("switzerland", "austria", "germany", "belgium", "netherlands", "luxembourg", "liechtenstien", "italy", "portugal", "spain", "czech republic", "slovenia")

try:
    age = input("What is your age")
    age = int(age)
    country = input("what is your country? ")
    Hard_liquour = ("gin", "vodka", "whiskey", "rum", "tequila", "absinthe", "sake")
    if age >= 21:
        legal = True
    elif age >= 18 and (country != "USA" and country != "UAE"): # has to be other than these two
        legal = True
    elif age >= 16 and country == ("Luxembourg":
        legal = True
except ValueError:
    print("Don't play games with me")

while
if legal:
    print("Dear", name, "It's my pleasure to serve you")
          drink_choice = input("what would you like? ")
    if drink_choice == Hard_liquour and country == beer_country:
        print("sorry, please choose something else")
else:
    print("Dear", name, "Unfortunately I cannot serve you today")