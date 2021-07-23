#Real Life Problems

'''Task 1:  Delivery Charges'''
print("***** Task 1: *****")
print()
# Create a program that takes the following input from the user:
# - The total number of sand sack and cement sack 
# -  Weight of each sack [Hint: use for loop to get the weight]
# - Use a variable to which the weight of the sack gets added as entered [Hint: calculate this within the for loop]
# - Calculates the total cost if each sack cost INR 300 [ outside the for loop]
# So let's get started

# sacks = int(input("Enter the total number of sacks: "))
# totalweight = 0
# for i in range(sacks):
#   weight = float(input("Enter the weight of every sack: "))
#   totalweight = weight + totalweight
# cost = sacks * 300
# print("Here is your cost: ", cost)
# print("Here is your total weight: ", totalweight)



'''Task 2:   Lets go Outdoors'''
print("***** Task 2: *****")
print()
#Write a program that takes care of outdoor field trips for kids.
# The program needs to:
# - Take the total number of kids (Number cannot be more than 8)
# - Get the name, and address for each kid
# The program must display the total cost for the field trip where
# - Cost for food for each kid is INR 500
# - Cost for travel for each kid is INR 1000

number = int(input("Enter the total number of kids: \nThis number cannot be more than 8."))
if number <= 8:
  for i in range(number): 
    name = input("Enter the child's name: ")
    address = input("Enter the child's address")
  food = number * 500
  travel = number * 1000
  print("Here is your cost for food: ", food, "\nHere is your cost for travel", travel,)
else: 
  print("Please enter a number that is less than or equal to 8!")
