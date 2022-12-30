#Defining a function
#_1
from cgitb import text
from hashlib import new
from tarfile import USTAR_FORMAT


def print_umar():
    print("we are learning with aamar")
    print("we are learning with aamar")
print_umar()
# #_2
def print_umar():
    text="we are learning with aamar"
    print(text)
    print(text)
print_umar()
#_3
def print_umar(text):
    print(text)
    print(text)
print_umar("we are learning with ammar")


# #defining a function with if,elif and else statment

def school_calculator(age,text):
    if age==5:
        print("Usama is join the School")
    elif age>5:
       print("Usama is should go to higher secoundary school")
    else:
       print("Usama is still a baby")
school_calculator(20, "Usama")

# define a function of future
def future_age(age):
    new_age=age+20
    return new_age
    print("new age")

future_age_predication=future_age(18)
print(future_age_predication)