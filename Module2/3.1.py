# In the previous lesson, you used if-elif-else statements to create a menu based program.
# Now let us take a look at using nested if-elif statements in creating menu based programs.
'''Task 1: Nested If-else'''
print()
print("*** Task 1: ***")
print()
#Make a variable like winning_number and assign any number to it between 1 and 20.
#Ask user to guess a number between 1 and 20. (Take input)
#if user guessed correctly, print "YOU WIN"
#if user didn't guessed correctly then:
  #if user guessed lower than actual number, then print "TOO LOW"
   #if user guessed lower than actual number, then print "TOO HIGH"

# winner = 17
# ask = int(input("enter your guess: "))
# if ask == 17:
#   print("YOU WIN!!!")
# else:
#   if (ask < winner) and (ask >= 1) :
#     print("TOO LOW!!!")
#   elif (ask > winner) and (ask <= 20) :
#     print("TOO HIGH!!!")
#   else:
#     print("Please enter a number from 1-20")




'''Task 2: Nested If-else'''
print()
print("*** Task 2: ***")
print()
#This is a program to tell User the shipping cost based on the country and the weight.
#Write a Program that takes two inputs: country_code(AU/US) and weight of the product.
#Use the following conditions to find the shipping cost
#country          Product Size               Shippping cost
#US               less than 1kg               $5
#US               between 1 and 2kg           $10
#US               greater than 2kg            $20
#AU               less than 1kg               $10
#AU               between 1 and 2kg           $15
#AU               greater than 2kg            $25

# print("This Program will caluculate Shipping Cost")

country_code = int(input("Enter your country code:\n1. US\n2. AU\n"))
weight = float(input("Enter weight: "))
if country_code == 1:
  if weight <= 1:
    print("Shipping Cost = $5")
  elif weight < 2 :
    print("Shipping Cost = $10")
  elif weight >= 2:
    print("Shipping Cost = $20")  
  else:
    print("Enter a weight greater than zero")
elif country_code == 2:
  if weight <= 1:
    print("Shipping Cost = $10")
  elif weight < 2 :
    print("Shipping Cost = $15")
  elif weight >= 2:
    print("Shipping Cost = $25") 
  else:
    print("Enter a weight greater than zero") 
else:
  print("Enter a valid Country Code")
