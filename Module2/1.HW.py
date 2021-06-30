
'''-----Task 1: Grade Detector ------'''
print("****Task 1: ****")
print()
# write a program that takes a score as the input and then returns a grade.
# The program returns the following Grades:
#  90 or higher gets an “A”
#  80 - 89 gets a “B”
#  70 - 79 gets a “C”
#  60 - 69 gets a “D”
# Anything below a 60 receives an “F”

# Number_Grade = int(input("Enter your number grade: "))
# if Number_Grade >= 90:
#   print("A")
# elif Number_Grade >= 80:
#   print("B")
# elif Number_Grade >= 70:
#   print("C")
# elif Number_Grade >= 60:
#   print("D")
# else:
#   print("F")

# # You need to write the appropriate if statements, to generate the correct grades.


'''-----Task 2: FizzBuzz Game ------'''
print("****Task 2: ****")
print()
# Write a program to accept an integer from the user. 
# If the number is a multiple of 3, print "Fizz" 
# If the number is a multiple of 5, print "Buzz"
# If the number is a multiple of 3 and 5, print "FizzBuzz"
number = int(input("Enter your number: "))
if (number % 3 == 0) and (number % 5 == 0):
  print("FizzBuzz")
elif (number % 3 == 0):
  print("Fizz")
elif (number % 5 == 0):
  print("Buzz")
else:
  print("Your number is not divisible by 3 or 5.")