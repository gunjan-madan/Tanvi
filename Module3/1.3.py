# In one of the previous lessons, you used the print statement to create text art.
# Imagine using the while loop command and the print statements to generate some really awesome text art.
# Let's help Sam create some great text art. All set to give it a try!

'''Task 1: Pattern Printing'''
print("**** Task 1: ****")
print()
# Uncomment the statements below and click Run to see what is displayed
print("**pattern1**")
i=1
while(i<=5):
  print("*"*i)
  i=i+1
# Wow!! Wasn't that awesome!! Now if you want to reverse the pattern, how will you change the code to generate it?
print()
print()
i = 5
while (i >= 1):
  print("*" * i)
  i = i - 1




'''Task 2: Combination Pattern'''
print("**** Task 2: ****")
print()
# Ready for the next challenge!
# You just created two patterns. Try combining them and see what you get

i=1
while(i<=4):
  print("*"*i)
  i=i+1
i = 5
while (i >= 1):
  print("*" * i)
  i = i - 1

'''Task 3: Dazzling Diamond'''
print("**** Task 3: ****")
print()
# Challenge!! Lets write code to print pattern given below:
#*****  *****
#****    ****
#***      ***
#**        **
#*          *
#*          *
#**        **
#***      ***
#****    ****
#*****  *****

i = 5
s = 1
while (i >= 2):
  print("*" * i, " " * s, "*" * i)
  i = i - 1
  s = s + 2
i = 1
while(i <= 5):
  print("*" * i, " " * s, "*" * i)
  i = i + 1
  s = s - 2



'''Fantastic!! You have created some great art work!! You definitely have a wonderful creative side.'''


