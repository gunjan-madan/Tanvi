#Nested For Loops

'''Task 1:   Pattern Match'''
print("***** Task 1: *****")
print()
# Math πrate has been given a for loop and range function to create a pattern like the one given below:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# Can you help him create it?

rows=6
for i in range(1, rows):
  for j in range(i):
    print(i, end=" ")
  print()
  
  

''' Task 2: Number Match'''
print("***** Task 2: *****")
print()
# In this round, you need to print the below pattern:
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# User inputs the maximum number to be printed
# Display the numbers from 1 upto the maximum number
# Repeat the pattern 4 times
# Any ideas how would you do it? Did you notice the pattern ? Can you display the pattern using a single loop?
# Hint: We can do this by using 2 loops. One for printing the numbers from 1 till the number entered by the user on the same row. Second for printing the above row 4 times
# Give it a try 
maximum = int(input("Enter a maximum number: \n"))
for i in range(4):
  for j in range(1, maximum + 1):
    print(j, end = " " )
  print()