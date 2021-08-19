# A set is a collection which is unordered and unindexed. 
# Sets are written with curly brackets.

''' Task 1: Unique or Not '''
print("***** Task 1: *****")
print()
# In Python, you can use data structures called sets to perform operations like 
# - Combining items
# - Finding common items
# - Identifying unique items
# Uncomment the statements and click Run

containerA = {"circle", "heart", "rectangle","cloud","star","bolt","moon","triangle","smiley"}
print("Container A contains:\n",containerA )


print("***** Task 1: *****")
print()
# Create a similar set for containerB

containerB = {"arrow", "cloud", "banner", "triangle", "plus", "hexagon"}
print("Container B contains: \n", containerB)

''' Task 2:  Vowel Count ''' 
print("***** Task 2: *****")
print()
# Write a program to count number of vowels using sets in a given string
# The key steps to follow are:
# - Create a set of vowels  
# - Initialize a count variable to 0.
# - Using a for loop, check if the letter in the string is present in the set "vowel".
# - If it is present, the count variable is incremented.


def vowel(str):
  counter = 0
  vowels = ("a", "e", "i", "o", "u")
  for i in str:
    if i in vowels:
      counter = counter + 1
  print("Number of Vowels: ", counter)

talk = input("Enter your string: ")
vowel(talk)
  

''' Task 3:  Languages Galore '''
print("***** Task 3: *****")
print()
# Uncomment the statements below and click Run

lang={"Java","Python","C++","C#"}
# Add SQL to the set
lang.add("SQL")
# Add HTML and Perl to the set
lang.update(["HTML","Perl"])
#Number of items in the set
print("The total number of items :",len(lang))
print(lang)
#Remove C#
lang.remove("C#")

# Here is the description to the methods used in the statements
# add() - Adds an item to a set
# update() - Adds multiple items to a set
# len() - Determines how many items a set has
# remove() - Removes an item from the set

# Uncomment the statements below and click Run

lang1={"Java","Python","C++","C#","CSS"}
lang2={"HTML","Perl","CSS"}
print("Union: ",lang1 | lang2)
print("Common: ",lang1 & lang2)
print("Difference: ",lang1 - lang2)

# Here is the description of the operations used in the statements
# | means Union. It displays all items from both sets.
# & means Intersection. It displays items common to both sets
# - means Difference. The difference of the set lang1 from set lang2(lang1 - lang2) is a set of elements that are only in lang1 but not in lang2


''' Task 4: Dat(a)nalyst or Scientist '''
print("***** Task 5: *****")
print()
# Write a program detailing the skill set for a data scientist and data analyst.
# Create a set each for:
# - Data scientist - Python, R, SQL, Scala, Java, Hive
# - Data analyst -  Python, SQL, BI, Excel, Tableau, R
# Display the common skills between the two roles
# Display the skills unique to each role
# Add the following skills to each of the set:
# - Data scientist - Machine Learning, Hadoop
# - Data analyst - Statistics, NoSQL

scientist = {"Python", "R", "SQL", "Scala", "Java", "Hive"}
analyst = {"Python", "SQL", "BI", "Excel", "Tableau", "R"}
print("Common Skills: ", scientist & analyst)
print("Unique Skills: ", scientist - analyst)
print("Unique Skills: ", analyst - scientist)

scientist.update(["Machine Learning", "Hadoop"])
analyst.update(["Statistics", "NoSQL"])
print("science", scientist)
print("analyst", analyst)