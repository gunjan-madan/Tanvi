# Do you know what the Pythagoras Theorem is? 
# The Pythagoras theorem states that “In a right-angled triangle,  the square of the hypotenuse side is equal to the sum of squares of the other two sides“. 
# The sides of this triangle have been named as Perpendicular, Base and Hypotenuse.
# The hypotenuse is the longest side, as it is opposite to the angle 90°.

"""-------Task 1:  What's missing in the right angled triangle? ------"""
print(" ")
print("*** Task 1: ***")

# Write a program to calculate the hypotenuse or one of the sides of the right angled triangle.
Missing = input("Is the Hypotenuse Missing?\nPress 1 for Yes & 2 for No")
if Missing == "1":
  Side_1 = float(input("Enter Side 1: "))
  Side_2 = float(input("Enter Side 2: "))
  Hypo = ((Side_1**2) + (Side_2**2))**(1/2)
  print("Here is your Hypotenuse: ",Hypo)
elif Missing == "2":
  Hypo = float(input("Enter Hypotenuse: "))
  Side_1 = float(input("Enter Side 1: "))
  if Hypo < Side_1:
    print("The Hypotenuse cannot be smaller than Side 1.")
  else:
    Side_2 = ((Hypo**2)-(Side_1**2))**(1/2)
    print("Here is your Missing Side: ",Side_2)
else:
  print("Please enter a valid input.")



''' Awesome!! You have successfully created a Pythagorean Theorem calculator. Congratulations!!'''