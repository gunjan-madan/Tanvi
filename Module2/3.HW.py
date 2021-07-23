#Practice on Nested Else if

''' Task 1: Metric Convertor'''
print("**** Task 1:  ****")
print()
# Write a Metric Conversion program that converts from one metric to another metric.
# You can start with:
# 1. cm to inch (Hint: divide the cm value by 2.54)
# 2. inch to feet (Hint: divide the inch value by 12)
# 3. meter to kilometer (Hint: divide the meter value by 1000)
# You can add more to the list.
Type = int(input("Enter the type of measurement: \nUse 1 for cm to inch\nUse 2 for inch to feet\nUse 3 for meter to kilometer\n"))
if Type == 1:
  Measurement = float(input("Enter your measurement in cm: "))
  Answer =  Measurement / 2.54
  print("Your answer is ", Answer)
elif Type == 2:
  Measurement = float(input("Enter your measurement in inches: "))
  Answer = Measurement / 12
  print("Your answer is ", Answer)
elif Type == 3:
  Measurement = float(input("Enter your measurement in meters: "))
  Answer = Measurement / 1000
  print("Your answer is ", Answer)
else:
  print("Please enter a valid input!")