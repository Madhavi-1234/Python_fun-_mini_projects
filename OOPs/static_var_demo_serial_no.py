## static variabke ( serial no:) demo

class BankAccount:
    __counter = 1

    def __init__(self, account_holder, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

        self.sno = BankAccount.__counter
        BankAccount.__counter += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
            print("New balance:", self.balance)
        else:
            print("Please enter a valid amount")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Amount withdrawn:", amount)
                print("New balance:", self.balance)
            else:
                print("Insufficient balance")
        else:
            print("Please enter a valid amount")

    def check_balance(self):
        print("Your current balance is", self.balance)

    def account_status(self):
        if self.balance >= 10000:
            print("Premium Account")
        elif self.balance >= 5000:
            print("Decent Account")
        else:
            print("Low Balance")

person_1 = BankAccount("Ram", 101, 5000)
person_2 = BankAccount("Rose", 102, 55000)
person_3 = BankAccount("Shyam", 103, 2000)

print(person_1.sno)
print(person_2.sno)
print(person_3.sno)
