import China
import senegal

from China import cook as China_cook
from senegal import cook as senegal_cook, drink as drink_senegal

try:
    from romania import cook as romania_cook
except ModuleNotFoundError:
    print("sorry no romania cook bro")
from China import greet
import sys
import pandas
print("hello guys")
def greet():
    print("hello from Segoland")

def cook():
    print("We are making Cochinillo")


China.cook()
China.greet()
print(China.hello)
for p in sys.path:
    print(sys.path)

import LATAM.cuba.cook as Cuba_cook
import LATAM.Peru.cook as Peru_cook
import LATAM.mexico.jalisco.cook as jalisco_cook
import LATAM.mexico.yucatan.cook as yucatan_cook
