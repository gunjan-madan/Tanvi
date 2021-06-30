# You used the if elif statement to handle multiple conditions.
# What if you have 10 conditions to evaluate? Will you write 10 if..elif statements? 
# Is it possible to check for more than one condition in a single if statement or elif statement? 
# Let's check it out  


"""-----------Task 1:  All in One ---------------"""
# print(" ")
# print("*** Task 1: ***")
# # Do you know what are isosceles and scalene triangles? 
# # Write a program to check if a triangle is equilateral, scalene or isosceles.
# side_a = int(input("Enter your first side: "))
# side_b = int(input("Enter your second side: "))
# side_c = int(input("Enter your third side: "))

# if (side_a == side_b) and (side_b == side_c):
#   print("You have an equilateral triangle.")
# elif (side_a == side_b) or (side_b == side_c) or (side_a == side_c):
#   print("You have an isosceles triangle.")
# else:
#   print("You have a scalene triangle.")

"""-----------Task 1.2:  All in One ---------------"""
print(" ")
print("*** Task 1.2: ***")
#The program takes a number as an input
#Program shall check if the number is divisible by both 3 and 4

# number = int(input("Enter your number: "))

# if (number % 3 == 0) and (number % 4 == 0):
#   print("Your number is divisible by 3 and 4.")
# elif (number % 3 == 0):
#   print("Your number is divisible by 3.")
# elif (number % 4 == 0):
#   print("Your number is divisible by 4.")
# else:
#   print("Your number is not divisible by 3 or 4.")

# """---------Task 2:   Its raining Discount -------------"""
# print(" ")
# print("*** Task 2: ***")
# Your store is giving a discount on the total purchase amount based on customer membership. 
# Write a program that calculates the discounted amount based on the below mentioned conditions:
# If membership is silver, 5% discount
# If membership is silver+ or gold, discount is 10%
# If membership is gold+ or diamond, discount is 15%
# if membership is platinum membership discount is 20%

# membership = input("Enter your membership: ")
# purchaseAmount= float(input("Enter the amount of money spent: "))
# if membership.lower() == "silver":
#   discountedPrice=purchaseAmount * (95/100)
#   print("You get a 5% discount!", "Your final bill is ", discountedPrice)
# elif (membership.lower() == "silver+") or (membership.lower() == "gold"):
#     discountedPrice= purchaseAmount * (90/100)
#     print("You get a 10% discount!", "Your final bill is ", discountedPrice)
# elif (membership.lower() == "gold+") or (membership.lower() == "diamond"):
#   discountedPrice= purchaseAmount * (85/100)
#   print("Your discount is 15%!", "Your final bill is ", discountedPrice)
# elif (membership.lower() == "platinum"):
#   discountedPrice= purchaseAmount * (80/100)
#   print("Your discount is 20%!", "Your final bill is ", discountedPrice)
# else:
#   print("Sorry, you do not get a discount.", "Your final bill is ", purchaseAmount)







"""---------Task 3:   Theme Rides -------------"""
print(" ")
print("*** Task 3: ***")
# You are managing the ticket counter at Imaginika Theme Park. Based on the age of the entrant, you issue tickets for the rides"
# Age between 5 and 7 :Toon Tango, Net Walk
# Age between 8 and 12: Wonder Splash, Termite Coaster Train
# Age greater 13: Hang Glider, Wave Rider
# If the age criteria does not match they can go for the nature walks
# Write a program that grants access to the rides based on the age conditions.
age = int(input("Enter your age: "))
if (age >= 13):
  print("Hang Glider, Wave Rider")
elif (age >= 8):
  print("Wonder Splash, Termite Coaster Train")
elif (age >= 5):
  print("Toon Tango, Net Walk")
else:
  print("Nature Walks")