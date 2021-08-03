'''Task 1: Unique Identifier'''
print("****** Task 1: ******")
print()
# Mr.Beaver's poultry business is doing very well.
# He now realizes that he needs to create a unique ID for each of the livestock in his farm.
# He wants you to create a program where the ID generated will have:
# - The current year
# - A random selection of colour code [Colour codes to be used are:red,blue,pink,yellow]
#- A randomly generated number between 1 and 100
# - A random selection of special characters (Special characters to be used are: $,#,@,!) 
import random
import datetime
password = 0
color = ["red", "blue", "pink", "yellow"]
year = datetime.datetime.now().year
password = random.choice(color) + year + 
  
  



''' Task 2: Duplicate or not '''
print("****** Task2: ******")
print()
# Mr.Beaver has an initial list of furnitures to buy and is still adding to the list
# To avoid duplication, he wants you to write a program that detects if the item already exists in the list  
# If the item exists, display a message saying "Item exists"
# If the item does not exist, append the item to the list and display the entire list
# The existing list has the following items:  tables, chairs, bed, dresser