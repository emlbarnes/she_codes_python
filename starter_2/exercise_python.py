import csv

colours = []

with open("colours_20_simple.csv",encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)
        #print line
        colours.append(line)

print (colours)
#Q1
for colour_group in colours:
    print(f"{colour_group[0]} {colour_group[1]} {colour_group[2]}")    
#Q2
for colour_group in colours:
    print(f"{colour_group[2]}, HEX: {colour_group[1]}, RGB: {colour_group[0]}") 