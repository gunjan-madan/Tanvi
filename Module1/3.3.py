'''*****Task 1: BODMAS - Setting the order******'''
print(" ")
print("*** Task 1:***")


p=6 + 10 / 2                      #11
q=(6 + 10) / 2                    #8
r=2 + 3 * 5                       #17
s=(2 + 3) * 5                     #25
t=6 +(8 / 4) - 2 * 3              #2
v=(6 + (8 / 4) - 2) * 3           #18

print(p,q,r,s,t,v)

'''*****Task 2: Display the Report Card******'''
print(" ")
print("*** Task 2:***")
# Once exams get over we all wait for our report cards.
# You too can create one in Python.
# To start you need to follow the below steps:
# Get the marks for the following subjects from the user : English, Science, Math, Computer Science and History
# Find the total marks and calculate the percentage scored
# Display both the total marks and the average achieved 
# [Hint: Total marks scored divided by the number of subjects gives you the average]
English = int(input("Enter you English Grade:"))
Science = int(input("Enter you Science Grade:"))
Math = int(input("Enter you Math Grade:"))
Computer_Science = int(input("Enter you Computer Science Grade:"))
History = int(input("Enter you History Grade:"))
Total_Sum = (English + Science + Math + Computer_Science + History)
Total_Percentage = Total_Sum / 5

print("The total marks are: ",Total_Sum)
print("The total percentage is: ", Total_Percentage)