# Can we automatically calculate the  age of a person or find out if the current year is a leap year or not.
# Let's take a look.  

'''Task 1: All about dates'''
print("***** Task 1: *****")
print()
# Well!!Python has a module called datetime to work with dates and perform calculations.
# Uncomment the statements below and click Run

# import datetime
# x = datetime.datetime.now()
# print("The current date is: ", datetime.datetime.now())
# print("The date today is: ",x.day)
# print("The current month is: ", x.month)
# print("The current year is: ", x.year)
#print("The current timezone is: ", x.timezone)

# What do you think the program does? 
# Here is a list of some of the datetime functions that have been used in the above program:
# datetime.now()- Displays the current date 
# day - Displays the current date from the date returned by the datetime.now() function
# month - Displays the current month from the date returned by the datetime.now()
# year - Displays the current year from the date returned by the datetime.now()


'''Timezone '''
#By default Datetime will display UTC (Universal Time)
#To get time of a specific timezone, we need another module

# import datetime
# import pytz
# time_zone= pytz.timezone('US/Eastern')
# y= datetime.datetime.now(time_zone)
# print(y)

#List of all timezones
# for tz in pytz.all_timezones:
  # print(tz)

'''Task - Calculate age of the person'''
# Write a program that calculates the age of a person using the list of functions given in the table. 

# import datetime
# day = int(input("Enter your day of birth: "))
# month = int(input("Enter your month of birth: "))
# year = int(input("Enter your year of birth: "))

# x = datetime.datetime.now()

# if x.month > month:
#   yearly = x.year - year
#   monthly = x.month - month
# else:
#   yearly = x.year - year - 1
#   monthly = 12 + x.month - month

# print("Here is your age: ", yearly, "years old", monthly,"months old")



'''Task 2: Is it a leap year or not'''
print("***** Task 2: *****")
print()
# Write a program to find if the current year is a leap year or not
# Hint: Any year that is divisible by 4  or 400 is a leap year

# import datetime
# x = int(datetime.datetime.now().year)
# if (x % 4 == 0) or (x % 400 == 0):
#   print(x, "is a leap year")
# else:
#   print(x, "is not a leap year")

'''Task 3: Number of Days'''
print("***** Task 3: ****9*")
print()
# Write a program to display the number of days in the current month
# Hint: Use the datetime.datetime.now() function to get the month 

import datetime
x = datetime.datetime.now().month
if x in (1, 3, 5, 7, 8, 10, 12):
  print(x, "has 31 days")
elif x in (4, 6, 9, 11):
  print(x, "has 30 days")
else:
  print(x, "has 29 days")




'''Fantastic!! You are good at writing programs using the datetime module. Way to go!!'''