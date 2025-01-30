s = "hello"
print(dir(s))
useful_methods = [m for m in dir(s) if "__" not in m]
print(useful_methods)

print(help(s.capitalize))
print(s.capitalize())
print("hello".center(50,"*"))

print("I see a little dove". count("e")) # counts how many times does "e" show up
print("bananananananananananananananana".count("ana"))
x= "I do not cook nor compare"
print(f"There are {x.count("o")}os inside: '{x}'")

s = "bob goes home to meet bob so they can take their bob and go bobbing"
pos = 0
while True:
    start = s.find("bob", pos)
    if start == -1:
        break
    print("found bob on position", start)
    pos = start + 1

items = ["cat", "rat", "mouse", "house"]
print("+another+".join(items))
pint("I LIKE to go HIkIng!!".lower().upper())
print("i like to go skiing".title())
# replace, replaces item with item inside the string
print("i like to go skiing".replace("i", "1").replace("e","3"))
#split, makes a list of the tring split by the delimiter
print("I like to go skiing".split())
