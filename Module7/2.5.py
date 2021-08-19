''' Task 1: Three Dice '''
print("****** Task 1: ******")
print()
# The next game that Mr.Bumblebee has planned is called "Three Dice". 
# The rules of the game is as follows:
# - Each dice has three sides each.
# - Each of  side of the dice has the number 1, 2 and 3 printed
# - A player rolls  all the three dice. On rolling
# - If he gets all three of the same number, the program displays "Rollzee"
# - If he gets two of the same number, the program display "Two of a kind"
# - If he gets one of each number, the program displays "One of a kind".
# The player gets to roll the dice as long as he wants.
# If he wants to quit the game, he needs to type "Exit"

# import random
# quit = int(input("If you want to play, press 1\nIf you want to quit, press 2"))
# dice={"dice1":0,"dice2":0, "dice3":0}
# while quit != 2:
#   for i in dice:
#     dice[i]=random.randint(1,3)
#   if (dice["dice1"] == dice["dice2"] == dice["dice3"]):
#     print("Rollzee")
#   elif (dice["dice1"] == dice["dice2"]) or (dice["dice2"] == dice["dice3"]) or (dice["dice1"] == dice["dice3"]):
#     print("Two of a kind")
#   else:
#     print("One of a kind")
#   quit = int(input("If you want to play, press 1\nIf you want to quit, press 2"))


''' Task 2: What's the capital? '''
print("****** Task 2: ******")
print()
# The final game of the community event is “Guess the Capital”.
# You have created a similar program in your earlier “if-else” lesson. 
# You can either change that program or use the list below to create a new program.
# Here is the list of the country and its capitals:
# India - New Delhi
# Afghanistan - Kabul
# Brazil - Brasilia
# Canada - Ottawa
# Indonesia - Jakarta
# Ireland - Dublin
# Netherlands - Amsterdam
# Norway - Oslo
# Turkey - Ankara
# Vietnam - Hanoi
# Mr.Bumblebee want you to create a game where :
# - A player has to guess the capital of the country
# - For each correct answer, the player gets one point
# - At the end of the game, the total score needs to be displayed

countries = {
"India" : "New Delhi", 
"Brazil" : "Brasilia", 
"Afgjanistan" : "Kabul", 
"Canada" : "Ottawa", 
"Indonesia" : "Jakarta", 
"Ireland" : "Dublin", 
"Netherlands" : "Amsterdam", 
"Norway" : "Oslo", 
"Turkey" : "Ankara", 
"Vietnam" :"Hanoi" }
counter = 0
for i in countries:
  print("What is the Capital of ", i, "?")
  quest = input().lower()
  if quest == countries[i].lower():
    counter = counter + 1
    print("Correct")
  else:
    print("Incorrect")

print("Final Score :", counter)
