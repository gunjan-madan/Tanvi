'''*****Task 1: Arithmatic Calculator*****'''
print(" ")
print("*** Task 1:***")
# Extend the additive calculator to a basic Math calculator
# Write a program that does the following:
  # 1. Accept two integers from the user 
  # 2. Display separately on three lines: 
  # 3. The sum of the two numbers. 
  # 4. The difference of the two numbers (first - second). 
  # 5. The third line contains the product of the two numbers

Number_1 = int(input("Enter your 1st integer: "))
Number_2 = int(input("Enter your 2nd integer: "))
Sum = Number_1 + Number_2
Difference = Number_1 - Number_2
Product = Number_1 * Number_2
print(Sum)
print(Difference)
print(Product)

'''******Task 2:  Grocery Checkout : Lets get calculating******'''
print(" ")
print("*** Task 2 :***")
# Ready for a role play.
# You work at the "Freshmart Grocery Shop" as an accountant
# Your manager has given you the following rate card:
# 1 kg of cauliflower - Rs. 30
# 1 kg of potato - Rs. 15
# 1 kg of Onion - Rs. 20
# 1 kg of Beans - Rs 25
# This week happens to be the discount week for customers. 
# You need to give the customer a discount of 10% on the total purchase.
# You have a customer who has bought:
# 2 kg of potato
# 1 kg of onion
# 1 kg of beans 
# 2 kg of cauliflower
# Write a Python program to calculate the amount the customer needs to pay.

Potato = int(input("Enter the number of potatoes: "))
Onion = int(input("Enter the number of onions: "))
Beans = int(input("Enter the number of beans: "))
Cauliflower = int(input("Enter the number of cauliflower: "))
Sum = (15 * Potato) + (20 * Onion) + (25 * Beans) + (30 * Cauliflower)
Discount = (90/100) * Sum
print("Here is your total: ", Discount)