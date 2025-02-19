
print("Q9")
def days_since_bday(birthday, current_year):
    """
    gets the year, calculates the years passed, counts number of leap years, then calculates days passed given leap years
    :param birthday:
    :param current_year:
    :return:
    """
    birth_year = int(birthday[-4:])  # 4 characters are the year
    years_passed = current_year - birth_year - 1
    leap_years = 0
    for year in range(birth_year + 1, current_year):  # exculde current and birth year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  #check if leap year
            leap_years += 1 # count leap years
    days_passed = (years_passed * 365) + leap_years
    return days_passed

print("Days since my birth date:", days_since_bday("03-09-2003", 2024))

print("Q8")
def is_valid_url(url):
    """
    We use a list of valid url beginnings and ending to check, since we dont have libraries of the known we just write the common known,
    just to demonstrate the use case, then check for both noting TRUE and FALSE, if they have both they will be considered as valid urls when printing the list
    :param url:
    :return:
    """
    valid_starts = ["http://", "https://", "www."] # valid URL beginnings
    valid_endings = [".com", ".org", ".net", ".edu", ".gov"] # valid URL endings

    has_valid_start = False # check whether the start is valid
    for start in valid_starts:
        if url.startswith(start):
            has_valid_start = True
            break

    has_valid_end = False # check whether the end is valid
    for end in valid_endings:
        if url.endswith(end):
            has_valid_end = True
            break

    return has_valid_start and has_valid_end

urls = ["http://coolstuff.com","https://warhammer40k.org","www.pathofexile.com","ftp://stuff.net","stuff.xyz","chicken.com"] # test examples

for url in urls:
    print(url, "VALID" if is_valid_url(url) else "NOT VALID")


print("Q7")
import random
numbers = [] # create empty list
for i in range(10):
    numbers.append(random.randint(1, 100))  #append numbers into list
processed_numbers = []  #new list to store the processed numbers, without odd and doubled evens
for num in numbers:  # check all numbers
    if num % 2 == 0:  # check if even
        processed_numbers.append(num * 2)  # add and double

print(processed_numbers)

print("Q6")
# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits[1] = "orange"  # replacing
print("modified fruits:", fruits)  # succesful mutation


# Strings
s = "hello"
print(s)
try:
    s[0] = "y"  #to show that strings cannot be modified
except TypeError as e:
    print("Error:", e)

print("Q5")
text = "unlikely ungan ushakey unopened unpleasant unman"
def count_of_pattern(text): #defining the function
    """
    Checks whether the text in text meets the requirements, adds to count if it does and then prints the total count at the end
    :param text:
    :return:
    """
    count = 0
    words = text.split() #split the list of words using the spaces
    for word in words: #checks each word in list
        if word.find("un") == 0 and word.rfind("an") == len(word) - 2: # if the word meets the requirement defined then increase the count
            count += 1
    return count

print(count_of_pattern(text))  # print the count

print("Q4")
words = [
    "6892149109325320763773670235239019412986",
    "1414884937242655719669145562427394884141",
    "6800923757255865070000705685527573290086",
    "9847255590886266818998186626880955527489" ]
for word in words:
    if word == word[::-1]:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")


print("Q3")
import datetime
a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

print("Q2")
print((2+3)*6/2 and 18.0)

print("Q1")
a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3
print(a)
