#while loop along with if conditions

# Have you been to a game arcade? 
# Which of the games are your favourite? 
# Are you ready to design one?
''' Task 1: Number Buzzer Game'''
print("**** Task 1: ****")
print()
# Write a “Guess the Number”  game, where a player has to guess a number between 10 and 20.  Let's assume that the number to guess is 15.
# Let's add some checks to the game, you have written:
# If the number is lesser than 10, you must give a warning message and ask them to guess again
# If the number is greater than 20, you must give a warning message for the same and ask them to guess again
# If the number is right, then you display a congratulatory message

# counter = int(input("Enter your guess between 10 & 20: "))
# while counter != 15:
#   if (counter < 10) or (counter > 20):
#     print("The number must be between 10 & 20.")
#     counter = int(input("Enter your guess between 10 & 20: "))
#   else:
#     print("Try Again!")
#     counter = int(input("Enter your guess between 10 & 20: "))

# print("YOU GUESSED THE NUMBER!")


''' Task 2: Break the loop'''
print("**** Task 2: ****")
print()
# Now let's bring in a twist in the program you wrote in Task 1. # You need to modify the program, in a way that it allows only 3 chances to guess the number.

# number = 1
# while number <= 3:
#   counter = int(input("Enter your guess between 10 & 20: "))
#   if (counter < 10) or (counter > 20):
#     print("The number must be between 10 & 20.")
#   elif counter == 15:
#     print("YOU GUESSED THE NUMBER!")
#     break
#   else:
#     print("Try Again!")
#   number = number + 1


''' Task 3: To quit or not to quit'''
print("**** Task 3: ****")
print()
# Write a program that takes numbers between 1 and 100 from the user.
# To quit entering numbers the user needs to press 0. 
# The program should then display the sum and the product of the numbers
number = 1
sums = 0
product = 1
while number != 0:
  number = float(input("Enter your number:\nPress 0 to quit\n"))
  if number == 0:
    break
  elif (number < 1) or (number > 100):
    print("Please enter an number between 1 and 100")
    continue
  sums = sums + number
  product = product * number
  
  
print("Here is your product: ", product,"\nHere is your sum: ", sums)