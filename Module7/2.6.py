# Mr.Beaver and Mr.Bumblebee have opened a farm market.
# They need your help for the following tasks:
# Task 1: Create inventory stock of items
# Task 2: Create the price list for the items
# Task 3: Get the shopping list
# Task 4:Create a function that generates the bill. The bill should take into consideration
# - Checking the inventory stock 
# - Checking the price list

'''Task 1: Create Inventory Stock'''
print("****** Task 1: ******")
print()
# Create a dictionary with items and their stock.
# You can start with the following items:
# Banana - 10
# Apple - 15
# Orange - 32
# Pear - 15
# Print the stock after creating the dictionary

items = {"banana" : 10, "apple" : 15, "orange" : 32, "pear" : 15}
print(items)

'''Task 2: Create the price list'''
print("***** Task 2: *****")
print()
# Create a dictionary that stores the price for the items.
# Here is the price for the items:
# Banana - 20
# Apple - 80
# Orange - 60
# Pear - 90

pricing = {"banana" : 20, "apple" : 80, "orange" : 60, "pear" : 90}
print(pricing)

'''Task 3: Getting the Shopping List'''
print("***** Task 3: *****")
print()
# Write the code to get the quantity of each item from the user.
# If the user does not want a particular item, they need to enter 0.
# Hint: Create a copy of the item list and get the user to enter the quantity for each item.


shop = items.copy()
for i in shop:
  print("Enter your order for ", i )
  order = input()

  shop[i] = int(order)
  if order == 0:
    break
print(shop)


'''Task 4: Compute the Bill'''
print("***** Task 4: *****")
print()
# Create a function to calculate the total price for items ordered.
# The function must:
# - Check the stock of items
# - Display the total price

def bill(shoppinglist):
  price = 0
  for i in items:
    if shoppinglist[i] > items[i]:
      print(i, ": Out of Stock")
    else:
      price = price + shoppinglist[i] * pricing[i]
  print("Here is your price: ", price, "\nPrice for out of stock items not included.")
      
bill(shop)

'''Brilliant!! You have automated the inventory related tasks.. Awesome!!'''