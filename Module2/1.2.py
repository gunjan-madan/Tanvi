#Lets Learn using multiple conditions


"""-----Task 1:  What is your score? ---------"""
print(" ")
print("*** Task 1: ***")
# Write a program to get the marks for Mathematics from the user. 
# If the marks is less than 50 or equal to 50, print a message saying “you need to improve”.
# If the mark is between 50 and 80, print “ Let's work little more!”
# If the mark is more than 80, print “ You are doing good. Keep it up!”
# marks = int(input("Enter your grade: "))
# if marks <= 50:
#   print("You need to improve.")
# elif marks <= 80:
#   print("Let's work a little more.")
# else:
#     print("You are doing good. Keep it up!")

"""-----Task 2:  Which sides are equal? ---------"""
print(" ")
print("*** Task 2: ***")
#In this program we will take three sides of a triangle as input from user
#Compare the sides to check if they are equal
side_a = int(input("Enter your first side: "))
side_b = int(input("Enter your second side: "))
side_c = int(input("Enter your third side: "))

if side_a != side_b:
  print("Your first side does not equal your second side.")
elif side_b != side_c:
  print("Your second side does not equal your third side.")
else:
  print("All 3 sides are equal")