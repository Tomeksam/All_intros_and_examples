print(not True)
print(not False)
print(not 7) # False because 7 is True, not checks for not true

print(True or False)
print(True and False)
print(2 or 3 or 4) # first true is the one that is printed, as its the first that satisfies the condition
                   # if all are false then its the last one, "last one that couldve been True"


print(1 and 2 and 3) # first False that you encounter, or last if all are True
print(1 and 0.0 and 4) # 0.0 is the first False, despite that 4 may be True
print(2 and 3 and 1)