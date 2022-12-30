# #while and For loops


#  #while loops

from re import X


x=0
while (x<=5):
     print(x)
     x=x+1

# # for loop


for x in range(4,11):
    print(x)


#array
days=  ["Mon","tue","wed","thu","fri","sat","sun"]

for d in days:
    if (d=="fri"): break   #loop stop
    print(d)