# Have you wondered what would happen if you had an infinite loop? 
# It is important to break away from an infinite loop else, the computer keep processing without any end
# Let us take a look at some programs that help break from a loop

'''Task 1: Whats the price '''
print("**** Task 1: ****")
print()
# Write a program that takes the price of goods sold as inputs from the user.
# To stop entering or when the user is done, he or she news to press 0.
# Once the user is done,the program must print
# - Total cost  of the goods 
# - Total number of goods.

print("Enter 0 to stop when you are done entering")
cost = 0
number = 0
Price = 1
while Price != 0:
  Price = float(input("Enter the price: "))
  number = number + 1
  cost = cost + Price
print("Here is your total cost: ", cost)
print("Here is your number of items: ", number)
 



'''Task 2: Lemonade and Glasses '''
print("**** Task 2: ****")
print()
# Your friend Sam has a jar with 5 cups of fresh lemonade.  
# Jack has some glasses which hold 1.5 cups each of liquid.  
# How many glasses of lemonade can Jack serve?
cup = 3
glasses = 0
total = 15
while total > 0:
  total = total - cup
  glasses = glasses + 1
print(glasses)
'''Task 3: Population Calculator '''
print("**** Task 3: ****")
print()
# Sam is thrilled how he is able to solve problems
# He now wants to solve a population projection problem
# Can you solve it for him?
# He wants to know how long will it take to reach a certain target population (in years), given a 
# - starting population =10000000
# - birthrate=0.015
# - deathrate=0.023
# - Reduction can be taken as 0.1.
# Hint1: Target population can be calculated as population * reduction
# Hint2: Change in population can be calculated using the formula (current_pop * birthrate) - (current_pop * deathrate)

birthrate = 0.015
deathrate = 0.023
starting_pop = 10000000
years = 0
target = starting_pop * 0.1
while starting_pop >= target:
  change = (starting_pop * birthrate) - (starting_pop * deathrate)
  starting_pop = starting_pop + change
  years = years + 1
print("Here is your time: ", years)





'''Great! You are exceptionally good at coming out with programming solutions. Way to go!!'''