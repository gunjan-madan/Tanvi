# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.


'''Task 3: Filter it out'''
print("***** Task 3: ******")
print()
# Uncomment the code below to check how filter works
# list of letters
# letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# filtered_vowels=[]
# # function that filters vowels
# def filter_vowels(letter):
#     vowels = ['a', 'e', 'i', 'o', 'u']

#     if(letter in vowels):
#         return True
#     else:
#         return False

#Write code to add only vowels to filtered_vowels list from letters using function filter_vowels

'Using Filter functions'
#The same functionality can be achieved using filter:
# filtered_vowels = list(filter(filter_vowels, letters))
# print(filtered_vowels)

'Using Lambda functions'

# filtered_vowels=list(filter(lambda letter: letter in ['a','e','i','o','u'] , letters))

# print(filtered_vowels)


'Task'
# Write a program that:
# - Filtered the list given below to find IDs which contain only numbers
# - Prints the result . 
# ids=["MN203", "35434", "23466","VG234","12345", "F3456", "85767"]
