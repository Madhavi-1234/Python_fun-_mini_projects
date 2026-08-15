
print("Hi, Plaese enter you password"
"Read instructions"
"Length at least 8 "
"At least 1 uppercase letter"
"At least 1 lowercase letter"
"At least 1 digit"
"At least 1 special character (@, #, $, %, !, etc.)"
)
## id passoword valid or not ?
def is_valid_pass(password):

    if len(password) < 8:
        return False

    upper = False
    lower = False
    digit = False
    special = False

    special_chars = "@#$%!"

    for char in password:

        if char.isupper():
            upper = True

        elif char.islower():
            lower = True

        elif char.isdigit():
            digit = True

        elif char in special_chars:
            special = True

  
    if upper and lower and digit and special:
        return True
    else:
        return False


password = input("enter your password: ")
print(is_valid_pass(password))
