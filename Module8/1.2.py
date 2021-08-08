# Python’s map() is a built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop,


'''Task 1: Map the result'''
print("***** Task 1: ******")
print()
# Write the code to prepare a final list which has squares of all the numbers in the given list.
# initialList=[2,4,5,3,7]
# finalList=[]


'using map function'

# def square(number):
#   return number**2

# finalList= list(map(square,initialList))
# print(finalList)

'using lambda function'

# finalList=list(map(lambda x: x**2, initialList))
# print(finalList)

'Iterating using multiple lists'
#Map function can take multiple lists as input.
#The final iterable is only as long as the shortest iterable
# list1=[1,2]
# list2=[4,5,6]

# final= list(map(lambda x,y: x+y, list1,list2))
# print(final)

'''Task 2: Map multi lists'''
print("***** Task 2: ******")
print()
# Write a program that : 
# - Takes a list of 
# --> base numbers (For example: 10, 20, 40, 50 etc.)
# --> index numbers (For example: 1, 2, 3, 4 etc.)
# - Returns a list  containing the power of each number in the base raised to the corresponding number in the index
