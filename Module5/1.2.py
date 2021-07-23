# You have just learnt how to use built-in functions with numbers.
# Let’s take a look at how to use built-in functions on strings.

'''Task 1: upper and lower '''
print("***** Task 1: ***** ")
print()

# Let us use the lower() function.
txt="Hello, New House Owner!"
txt1=txt.lower()
print(txt1)

# Let us use the upper() function.
txt2=txt1.upper()
print(txt2)

# Here we will use the replace() function. Uncomment the statement below and execute it.
txt3 = txt2.replace("H", "M", 1)
print(txt3)

#The format of replace function is as follows:
#  string.replace(oldvalue, newvalue, count). Here 
#   - oldvalue is the string to search for
#   - newvalue is the string replace the old value with
#   - count is optional and is a number specifying how many occurrences of the old value you want to replace. Default is all occurrences

# Here to split, the separator is the", ". So let us use the split() function. Uncomment the statement below and execute it.
x = txt.split(", ")
print(x)

'''Task 2: What's the code? '''
print("***** Task 2: ***** ")
print()
# Given below is the code to enter a new house.
# Coded password is: "Hello My Master, I am your New House."
# Write a program to do the following:
#  - Convert it into upper case
#  - Replace word “House” with “AppleTree”
#  - Split the message, where in the separator is the", ".

hello = "Hello My Master, I am your New House"
print(hello.upper())
y = hello.replace("House", "AppleTree")
print(y)
z = hello.split(",")
print(z)

'''More functions '''
name = "gunjan"
value ="12"
space="  "
print(name.isupper())
print(name.islower())
print(len(name))
print(name.isnumeric())
print(value.isnumeric())
print(space.isspace())

# Here is a list of the functions we used in the program
# string.isupper() - The isupper() function returns True if all the characters are in upper case, otherwise False.
# string.islower() - The islower() function returns True if all the characters are in lower case, otherwise False.
# len(string) - The len() function returns the number of characters in the string.
# string.isspace() - The isspace() function returns True if all the characters in a string are whitespaces, otherwise False.
# string.isnumeric() -The isnumeric() function returns True if all the characters in the text are numeric

'''Task 3: Secret Code '''
print("***** Task 3: ***** ")
print()
# Studmonkey has set some instructions for anyone entering the kitchen: 
# - User to provide their first name and surname/last name in upper case:
# - User to provide their first name and surname/last name in upper case
# - User to provide their age. The age should be a double digit like 13, 14, 22 etc.
# - User to provide a secret code word which they will use each time they enter the kitchen. The code word should not have any space and should be in lower case

# quest = input("Do you want to enter the kitchen? \n1 for Yes \n2 for No")
# while quest == "1":
#   first = input("Enter your first name: ")
#   last = input("Enter your last name: ")
#   if (first.isupper() == False) or (last.isupper() == False):
#     print("Your name must be uppercase!")
#     break
#   age = input("Enter your age: ")
#   if len(age) < 2 or age.isnumeric() == False:
#     print("The age must be in double digits and a number. ")
#     break
#   code = input("Enter your secret code: ")
#   if (code.isspace() == True) or (code.islower() == False):
#     print("Your code word should have no spaces and everything should be lower case.")
#     break
#   print("Welcome to my Kitchen")  
#   break

'''Task 4: Ready for an adventure '''
print("***** Task 4: ***** ")
print()
# You are in charge of  taking in applications for the Summer Adventure workshop. You need to ensure that when applying students:
# - Enter their full name in upper case
# - Enter a valid age
# - Provide an email address and not leave it empty

app = input("Are your applying for the Summer Application Workshop? \nEnter 1 for Yes or 2 for No: ")
while app == "1":
  name = input("Enter your full name in uppercase: ")
  if name.isupper() == False:
    print("Make sure your name is uppercase! ")
    continue
  email = input("Do not leave this blank empty \nEnter your email address: ")
  if email.isspace() == True:
    print("Enter your email address!")
    continue
  age = (input("Enter your age: "))
  if (int(age) < 0) or (len(age) < 2):
    print("Enter a valid age!")
    continue
  else:
    print("Thanks for enrolling!")
    break




