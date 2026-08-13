print("1 --> Water")
print("2 --> Gun")
print("3 --> Snake")

computer = 3

user = int(input("Enter your choice: "))

if computer == 1 and user == 2:
    print("Computer wins")

elif computer == 2 and user == 3:
    print("Computer wins")

elif computer == 3 and user == 1:
    print("Computer wins")

elif computer == user:
    print("Draw")

else:
    print("You won")
