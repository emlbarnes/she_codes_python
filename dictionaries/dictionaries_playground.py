# groceries = {
#     "baby spinach": 2.78,
#     "hot chocolate": 3.70,
#     "crackers": 2.10,
#     "bacon": 9.00,
#     "carrots":0.56,
#     "organes":3.08
# }

# print(groceries)

# print(groceries["baby spinach"])
# print(groceries["crackers"])

# groceries["crackers"] = 1.5
# print(groceries)

# groceries["avocado"] = 3.0
# print(groceries)

# del groceries["bacon"]
# print(groceries)

# for item in groceries:   
#     # print(item)
#     print(f"{item}:${groceries[item]}")

# for item, price in groceries.items():
#     print(f"{item}: ${price}")


groceries= {
"Baby Spinach": 2.78,
"Hot Chocolate": 3.70,
"Crackers": 2.10,
"Bacon": 9.00,
"Carrots": 0.56,
"Oranges": 3.08
}

quantity = {
"Baby Spinach": 1,
"Hot Chocolate": 3,
"Crackers": 2,
"Bacon": 1,
"Carrots": 4,
"Oranges": 2
}

print(groceries)
for item, price in groceries. items():
    print(f"{item}: ${price}")

for item, in groceries.items():
    print(f"{item}:${price}")

for item, price in prices.items():
    total_cost = round(quantity[item] * price)
    print(f"{item} @ ${price} = {total_cost}") 