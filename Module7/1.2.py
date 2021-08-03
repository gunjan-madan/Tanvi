'''Task 1: What's the codeword?'''
print("****** Task 1: *******")
print()
# Mr.Beaver has kept a list of codewords for entry into his house
# Whoever guesses the code words at the entrance gate, is allowed to enter his house.
# The list of code words are:rainbow, butterfly, sunshine,cupcake
# Create a list of above codewords
# Take an input codeword from user
# Check if that matches from the list. If it matches, person can enter otherwise not

# codewords = ["rainbow", "butterfly", "sunshine", "cupcake"]
# usercode = input("Enter your codewords: ")
# flag= False
# for i in codewords:
#   if usercode.lower()==i:
#     flag= True
#     print("Codeword Matched!")
#     break
#   else:
#     flag=False
    
# if flag==False:
#   print("Incorrect Codeword!")


# if (usercode in codewords):
#   print("Codeword Matched")
# else:
#   print("Incorrect Password")



'''Task 2: Earn Your Brownie Points'''
print("****** Task 2: *******")
print()
# Mr.Beaver and his family visit the gym regularly. 
# There are four members in his family - Otto, Beth, Bob, Emma
# To ensure that each of them gets to exercise, Mr.Beaver has put a brownie points tally.
# The scores are calculated as follows:
# The brownie points are calculated at the end of the week and each one gets a goodie package, based on their score.
# 5 brownie points for exercising 1 to 3 hrs
# 10 brownie points for exercising 4 to 6 hrs
# Anything more than 6hrs, you get 15 brownie points.
# Can you help Mr.Beaver write a Python program that calculates the brownie points earned by each member in a week.
# Mr.Beaver wants a list that displays the name of the family member, hours worked and brownie points earned.
# For example [Otto, 3,5,Beth,5,10, Bob, 2,5,Emma,7,15]

# members = ["Otto", "Beth", "Bob", "Emma"]
# total = []
# for i in members:
#   print("Hi", i)
#   hours = int(input("Enter the hours exercised: "))
#   if (hours >= 1) and (hours <= 3):
#     brownie = 5
#     print("You get 5 brownie points.")
#   elif (hours >= 4) and (hours <= 6):
#     brownie = 10
#     print("You get 10 brownie points.")
#   else :
#     brownie = 15
#     print("You get 15 brownie points.")
#   total.append(i)
#   total.append(hours)
#   total.append(brownie)
# print(total)

# '''Task 3: Let’s string them together'''
# print("****** Task 3 : *******")
# print()
# # Mr.Beaver owns a poultry farm where he packs and supplies eggsHe packs in multiples of 5 or 10.
# # So the orders for Eg. are: 10 packs of 5 eggs  or 8 packs of 10 eggs.
# # The cost is then calculated as $2 per egg.
# # The list consisting of the following items is then shared with the customer: [name of the customer, total number of eggs,total cost]
# Write a program to help Mr.Beaver generate the list.
# Remember your program should allow for more than one customer entry.
exit = 1
packs = []
while exit != "0":
  name = input("Enter your name: ")
  eggs = int(input("Enter your package \nEnter 1 for pack of 5 eggs \nEnter 2 for pack of 10 eggs"))
  packages = int(input("Enter the number of packs:"))
  if eggs == 1:
    num = 5 
  else:
    num = 10 
 
  total = num * 2 * packages
  packs.append(name)
  packs.append(num * packages)
  packs.append(total)
  exit = input("Enter more orders: \nEnter 0 to Exit, Enter 1 to Continue")
print(packs)

