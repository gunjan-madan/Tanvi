#Lets learn using for loop along with strings
'''Task 1: Get Looping '''
print("**** Task 1: ****")
print()
# Using a for loop, print out each individual character in a string. 
# Uncomment the statements below and click on Run

text = "Looping"
for c in text:
  print(c,end=",")

# What if you want to display the characters, next to each other separated by a comma like:
# L,o,o,p,i,n,g
# For this all you need to do is add the following code in the print # statement like:



'''Task 2: Character Delimiter '''
print("**** Task 2: ****")
print()
#Use for loop and seperator to print alphabets in your name seperated by any special character.

text = "Tanvi"
for c in text:
  print(c, end = "!")

print()

'''Task 3: Find me if you can '''
print("**** Task 3: ****")
print()
# Write a program that takes the following input from the user:
# Any word, for example, plant
# A character to search in the word 
# The program needs to display the number of occurrences of the character searched for. [Hint: Use a counter variable]
# Now try the program by inputting a sentence and then searching for a character
# Did it work?

word = input("Enter your sentence or word: ").lower()
character = input("Enter your character: ").lower()
counter = 0
for c in word:
  if c == character:
    counter = counter + 1
print("Occurences of ", character, ": ", counter)

'''Task 4: You’ve got a mail '''
print("**** Task 4: ****")
print()
# write a program that asks the user to enter the email address for a promotional fun event
# The program needs to check if the email address entered is valid.[Hint: check if the user has used the character “@” only once] 

email = input("Enter your email address: ")
counter = 0
for c in email:
  if (c == "@"): 
    counter = counter + 1
if counter == 1:
  print("Email Submitted!")
else:
  print("Invalid Email Address")