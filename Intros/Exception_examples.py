name = input("What is your name? ") # Always add space to make it look better
print("Hello", name)
age = input("How old are you? ") # what if they enter something other than a number? My initial thought was doing an else statement to have a contingency, but my prof said that the pythonic way is just to try and see if there is going to be an error message
try:
    age = int(age)  # this will tell us here, use the TRY and EXCEPT method instead of stopping
    #new_age = age / 0
except ValueError:
    print("You are trying to trick me") #need to have the space before print, tabbed such that it goes under the
    print("Better luck next time")
except ZeroDivisionError:
    print("you cant divide by zero")
except:
    print("something unexpected happened")
else: # this happens if no error occurs
    print("You were probably born in", 2024-age)
finally:
    print("Thanks for playing along")