class Atm:
  def __init__(self):
    self.pin = ""
    self.balance = 0
    self.menu()

  def menu(self):
    while True: # Loop to keep the menu running until the user exits
      user_input = int(input("""\nHey, How would you like to proceed:
         1, Enter 1 to create pin
         2, Enter 2 to deposit
         3, Enter 3 to withdraw
         4, Enter 4 to check balance
         5, Enter 5 to exit
         """))

      if user_input == 1:
        self.create_pin()
      elif user_input == 2:
        self.deposit()
      elif user_input == 3:
        self.withdraw()
      elif user_input == 4:
        self.check_balance()
      elif user_input == 5:
        print('Exiting ATM. Goodbye!')
        break # Exit the loop
      else:
        print('Invalid choice. Please enter a number between 1 and 5.')

  def create_pin(self):
    self.pin = input("Enter your pin: ")
    print("Pin set successfully")

  def deposit(self):
    temp_pin = input("Enter your pin: ")
    if temp_pin == self.pin:
      try:
        amount = int(input("Enter your amount to deposit: "))
        if amount > 0:
          self.balance += amount
          print("Deposit successful!")
        else:
          print("Amount must be positive.")
      except ValueError:
        print("Invalid amount. Please enter a number.")
    else:
      print("Invalid pin")

  def withdraw(self):
    temp_pin = input("Enter your pin: ")
    if temp_pin == self.pin:
      try:
        amount = int(input("Enter your amount to withdraw: "))
        if amount > 0:
          if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
          else:
            print("Insufficient balance.")
        else:
          print("Amount must be positive.")
      except ValueError:
        print("Invalid amount. Please enter a number.")
    else:
      print("Invalid pin")

  def check_balance(self):
    temp_pin = input("Enter your pin: ")
    if temp_pin == self.pin:
      print(f"Your current balance is: {self.balance}")
    else:
      print("Invalid pin")

# Create an instance of the Atm class to run the program
atm = Atm()
