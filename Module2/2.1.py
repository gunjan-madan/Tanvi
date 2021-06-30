#Conditions along with Arithmetic operations


'''-----Task 1: Speed, Distance, Time Calculator------'''
print("****Task 1: ****")
print()
# Write a program which calculates the speed or distance or time depending on the inputs provided by the user
# Ask the user what they want to calculate and depending on the response, ask for the required inputs, 
# For example if the user says the speed needs to be calculated, take the distance and time as the input from the user

# Topic = int(input("Please Enter the Topic you want to Calculate\nPress 1 for Speed\nPress 2 for Distance\nPress 3 for Time"))
# if Topic == 1:
#   Distance = int(input("Enter your Distance: "))
#   Time = int(input("Enter your Time: "))
#   Speed = Distance / Time
#   print("Here is your speed: ", Speed)
# elif Topic == 2:
#   Time = int(input("Enter your Time: "))
#   Speed = int(input("Enter your Speed: "))
#   Distance = Speed * Time
#   print("Here is your distance: ", Distance)
# elif Topic == 3:
#   Speed = int(input("Enter your Speed: "))
#   Distance = int(input("Enter your Distance: "))
#   Time = Distance / Speed
#   print("Here is your time: ", Time)
# else:
#   print("Please enter a valid input!")

'''-----Task 2: Total Score------'''
print("****Task 2: ****")
print()
# Write a program that takes the Maths theory and Maths lab score. 
# Each of the score cannot be more than 50 
# Calculate the total score and print the result

theory = int(input("Please enter your theory grades: "))
lab = int(input("Please enter your lab grades: "))
if (theory <= 50) and (lab <= 50):
  total = theory + lab
  print("Here is total score: ", total)
elif (theory > 50) and (lab > 50):
  print("Make sure both scores are less than 50")
elif (theory > 50):
  print("Theory score cannot be greater than 50")
elif (lab > 50):
  print("Lab score cannot be greater than 50")
else:
  print("Please enter valid marks")
