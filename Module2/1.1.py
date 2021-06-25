# """-----------Task 1:  A Yes or A No ---------------"""
# print(" ")
# print("*** Task 1: ***")
# # Uncomment the statements and click Run
# print ("You have entered the Haunted Game Room")
# print ("Do you see a spooky figure?")
# answer = input("Type yes or no and hit 'Enter'.")
# if answer == "yes":
#   print ("You are entering the Jumpscare Mansion!! Your spooky friends are ready to surprise you")
# else :
#   print ("You are entering the Haunted Mansion garden!! Beware of the purple flowers!")


# """-----------Task 2:  Test the Condition ---------------"""
print(" ")
print("*** Task 2: ***")
# Write the program to find greatest number of two.
#Take two numbers as input from users and write the logic to find greatest.

Number_1 = int(input("Enter your 1st number: "))
Number_2 = int(input("Enter your 2nd number: "))
if Number_1 > Number_2  :
  print("Number 1 is greater than Number 2")
elif Number_1==Number_2:
  print("Number 1 equals Number 2.")
else :
  print("Number 2 is greater than Number 1")

"""-----------Task 3:  Even or Odd ---------------"""
print(" ")
print("*** Task 3: ***")
#DIY
#Asks the use to enter a whole number
#The Program shall check whether the number is even or odd.

# Num = int(input("Enter your whole number: "))
# if Num % 2 == 0 :
#   print("Your number is even.")
# else:
#   print("Your number is odd.")

# """-----------Task 4:  Whats in a frame? ---------------"""
# print(" ")
# print("*** Task 4: ***")
# # The program below asks the user to enter the length and breadth/width of a photo frame.
# If both the length and width are equal, the program prints "The photo frame is a square"
# If not  it prints "The photo frame is a rectangular"
# # Uncomment the statements below, write the code for the if and the print statements. [Hint: Use the == comparator]
# # Click Run to display the output
# a=int(input("Enter the length of the photo frame: "))
# b=int(input("Enter the breadth of the photo frame : "))
# if a == b:
#  print("The photo frame is a square." )
# else: 
#  print("The photo frame is a rectangle." )

# """------Task 5:  Positive or Not --------"""
# print(" ")
# print("*** Task 5: ***")
# Write a program to take a number as an input from the user.
# Check if the number is positive or negative
number = int(input("Enter your number: "))
if number > 0:
  print("Your number is positive.")
else:
  print("Your number is negative.")