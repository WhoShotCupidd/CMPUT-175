#!/usr/bin/env python3
# She Bang above is used to run through my compilier if it causes issues feel free to delete 

# This program has two functions: one that will use dictionaries to store information about a flower shop and display orders 
# the secondary function will take a txt input of earthquake data and display the data sorted to a seperate txt file
# ccid: clventer, name: Christiaan Lemmer Venter

# 1)

# Dictionary to store flower shop prices
springBulbs = {
    "daffodil" : "0.35",
    "tulip" : "0.33",
    "crocus" : "0.25",
    "hyacinth" : "0.75",
    "bluebell" : "0.50"
}

# 2)

# Dictionary to store flower shop orders
orders = {
    "daffodil" : "50",
    "tulip" : "100"
}

# 3)

# dynamiclly increase prices of flowers
springBulbs["tulip"] = round(float(springBulbs["tulip"])*1.25,2)

# 4)

# adding new flowers to the dictionary
orders["hyacinth"] = "30"

# 5)

# Calculate Subtotal of orders
subtotal = []
values = springBulbs.values()
keys = list(orders.keys())

for i in range(0,len(orders)):
    
    subtotal.append(float(list(orders.values())[i]) * float(springBulbs.get(keys[i])))

# Calculate Total of orders
for i in range(0,len(subtotal)):
    total = sum(subtotal)

# Sorting the flowers alphabetically
orders = dict(sorted(orders.items(), key=lambda x: x[0].lower()) )

# Displaying the orders
print("You have purchased the following bulbs: ")
for i in range(0,len(orders)):
    print("{0: <5} * {1: >4} = $ {2: >6.2f}".format((str(list(orders.keys())[i])[0:3]).upper(),list(orders.values())[i],subtotal[i]))

# 6)

# Displaying the total and how many bulbs purchased
for i in range(0,len(orders)):
    totalBulbsPurchased = sum(map(int,orders.values()))
print("")
print("Thank you for purchasing", totalBulbsPurchased, "bulbs from Bluebell Greenhouses.")
print("Your total is $", str(total) + ".")


# 2B Earthquake Data

# Intializing variables and file input
f = open("earthquake.txt", "r")

Alaska = ["ALASKA"]
Hawaii = ["HAWAII"]
Panama = ["PANAMA"]
Missouri = ["MISSOURI"]
Indonesia = ["INDONESIA"]
Vanuatu = ["VAUATU"]
Mexico = ["MEXICO"]

listOfregions = ["Alaska", "Hawaii", "Panama", "Missouri", "Indonesia", "Vanuatu", "Mexico"]

# For loop to sort the data into seperate lists 
for sentence in f:
    words = sentence.split()
    for i in range(0,len(listOfregions)):
        if words[-1] == listOfregions[i].upper():
            if i == 0:
                magAndDay = [words[1],float(words[0])]
                Alaska.append(magAndDay)
            elif i == 1:
                magAndDay = [words[1],float(words[0])]
                Hawaii.append(magAndDay)
            elif i == 2:
                magAndDay = [words[1],float(words[0])]
                Panama.append(magAndDay)
            elif i == 3:
                magAndDay = [words[1],float(words[0])]
                Missouri.append(magAndDay)
            elif i == 4:
                magAndDay = [words[1],float(words[0])]
                Indonesia.append(magAndDay)
            elif i == 5:
                magAndDay = [words[1],float(words[0])]
                Vanuatu.append(magAndDay)
            elif i == 6:
                magAndDay = [words[1],float(words[0])]
                Mexico.append(magAndDay)

# Appending each regions data to a parent list
largeList = [Alaska, Hawaii, Panama, Missouri, Indonesia, Vanuatu, Mexico]

# Creating a new file to write to and writing the data to the file in the order [Region, Day, Magnitude]
with open("earthquakefmt.txt",'w') as file:
    for i in range(0, len(largeList)):
        file.write(str(largeList[i]).replace("'","") + "\n")
        
# Closing the files
f.close()