#Chatbot
# Chatbot is a computer program that chats like a real person. For example Swelly is a Facebook Messenger chatbot.
# Take a look at this video, that shows what a conversational banking chatbot looks like:
# https://www.youtube.com/watch?v=SNQGypLBJys

'''Task 1: Product Inventory'''
print()
print("*** Task 1: ***")
print()
# You work in the inventory department of an Automobile company.
# You want to write a program that will help in:
# Taking the order quantity from the user and checking if there is enough stock of the item requested. [Hint: Set a value for the stock availability] 
# If there is then take the name, address and phone number from the user and let them know it will be sent to their address in 48 hrs.
# If not let the user know that, the item is not in stock and that they will receive an email once it is in stock
# Ensure that the user enters the name, phone and address

# print("Hello, Welcome to Automobile Company!")
# Name = input("Please enter your name: ")
# Address = input("Please enter your address: ")
# Phone = int(input("Please enter your phone number: "))
# Order = int(input("Please enter your order quantity: "))
# if Order > 1000:
#   print("Sorry, your item is not in stock...")
# elif Order <= 1000:
#   print("Your order will be shipped to your address in 48 hours")
# else:
#   print("Please enter a vaild input.")


'''------- Task 2: Flowers on a Click'''
print("*** Task 2: ****")
print()
# You have to write a program that asks a customer if they like bouquets 
# If yes, ask them to  select a flower bouquet of their choice. You can use the following to start with:
#  - Rose and Lily 
#  - Orchid and Tuberose
#  - Rose and Carnation 
#  - Carnation and Orchids 
# Once the customer specifies their choice, you need to:
#  - Tell them the cost
#  - Get their address
# And send a message that it will be delivered to that address and they can pay by card, cash or Google Pay
# If the customer does not like bouquets choice, tell them to visit the website

Opinion = input("Do you like bouquets?")
if Opinion.lower() == "yes":
  print("Select a flower bouquet (Select the number):")
  choice = int(input("1. Rose & Lilly\n2. Orchid & Tuberose\n3. Carnation & Orchid"))
  if choice == 1:
    print("Cost: 15.99")
  elif choice == 2:
    print("Cost: 13.99")
  elif choice == 3:
     print("Cost: 12.99")
  else:
    print("Please enter a valid input")
  Address: input("Enter your address")
  print("Your order will be delivered to your address")  
elif Opinion.lower() == "no":
  print("Check the website")
else:
  print("Enter yes or no")