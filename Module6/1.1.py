#Functions
#Functions are required to reuse the code

'''Task 1:  All about functions'''
print("****** Task 1: *****")
print()
# Uncomment  the statement below and click Run.

##Define a user-defined function
def welcome():
  print("Welcome to Cuemath Python class!!")
#Call the function
welcome()

'''Task'''
# Write a function to print your name and grade

# def info():
#   print("My name is Tanvi & I am in 10th grade.")
  
# info()

''' Task 2: Redefine the function '''
print("****** Task 2: *****")
print()
# Uncomment  the statements and click Run

# def studentdetails(name):
#  print("Name is:", name)
# studname=input("Enter your name: ")
# studentdetails(studname)
# Modify the program to:
# - Take the grade and age as input from the user
# - Pass the grade and age as arguments to the function

# def studentdetails(name,age,grade):
#  print("Name is:", name)
#  print("Age is:", age)
#  print("Grade is:", grade)
# studname=input("Enter your name: ")
# studage = input("Enter your age: ")
# studgrade = input("Enter your grade: ")
# studentdetails(studname, studage, studgrade)

''' Task 3:  Point of return '''
print("****** Task 3: *****")
print()
# Uncomment the statement and click Run

## Define the function
# def addition(x,y):
#  z=x+y
#  return z
# #Call the function
# num1=int(input("Enter the first number: ")) 
# num2=int(input("Enter the second number: "))
# print("The sum is: ",addition(num1,num2))

# The function : 
# - Takes two arguments as input
# - Adds them and returns the sum to the caller.
# A return statement helps the function pass data back to the caller.
# Modify the above function to take three arguments  and return their product

# def multiplication(x,y,z):
#  a = x * y * z
#  return a
# #Call the function
# num1=int(input("Enter the first number: ")) 
# num2=int(input("Enter the second number: "))
# num3=int(input("Enter the third number: "))
# print("The product is: ",multiplication(num1,num2,num3))

''' Task 4:  What goes around, comes around '''
print("****** Task 4: *****")
print()
# Create functions that take the radius as the argument and return the area and perimeter.

# def area(radius):
#   are = 3.14 * (radius)**2
#   return are

# def perimeter(radius):
#   peri = 2 * 3.14 * (radius)
#   return peri

# radius = int(input("Enter your radius: "))
# areaCircle = area(radius)
# perimeterCircle = perimeter(radius)
# print("Your area is ", areaCircle, "\nYour perimeter is ", perimeterCircle)

''' Task 5: Convert days to second '''
print("****** Task 5: *****")
print()
# Create a function that takes the number of days as an argument , converts it to seconds and returns the same.

def seconds(days):
  seconds = days * 3600 * 24
  return seconds
days = int(input("Enter your number of days: "))
secondconvert = (seconds(days))
print("days to seconds: ", secondconvert)