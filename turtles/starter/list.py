wines=["pinot","shiraz","merlot","chardonnay"]
print (len(wines))
wines.append("chablis")
print(wines)
print(wines[0])
print (wines[3])
print(wines[-1])
wines.remove ("chardonnay")
print (wines)

if "ssb" in wines:
    print ("shiraz is red.")
else: 
    print("is white.")
if len(wines)>4:
    print("i have a lot of wine to drink.")
else: 
    print("wine has calories.")
for item in wines:
    print (len(item))
    print (item) 
    print (f"I would like to drink {len(item)} bottles of {item}")
    

import random

fav_wine = random.choice(wines)
print(f"my favoruite bottle of wine is {random.choice(wines)}")