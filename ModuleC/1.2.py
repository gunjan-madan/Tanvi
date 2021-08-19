# Lets create ATM Machine program/


''' Task 1:  Attributes and Functions of Bank Class '''
print("***** Task 1: *****")
print()
# Identify the attributes and functions of a Bank Class
# Graphically represent the same on a paper

# Attributes
# - Customer Name
# - Credit Card Number
# - Balance
# - Account Type

# Functions
# - Check Balance
# - Withdraw Money
# - Deposit Money

''' Task 2:   Banking in Action '''
print("***** Task 2: *****")
print() 
# Using the class design you have specified in Task 1 create the: 
# - bank class 
# - attributes and methods of the bank class

class bank:
  def __init__(self, name, card, balance, account_type):
    self.name = name
    self.card = card
    self.balance = balance
    self.type = account_type

  def checkBalance(self):
    print("Balance: ", self.balance)
  
  def withdraw(self,amount):
    if self.balance > amount:
      self.balance = self.balance - amount
      print("Updated Balance: ", self.balance)
    else: 
      print("Balance is low. You cannot withdraw this amount.")

  def deposit(self,amount):
    self.balance = self.balance + amount
    print("Updated Balance: ", self.balance)

a = bank("Sue", "1562763", 678, "Savings")
a.checkBalance()
