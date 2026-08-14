## check whether prime or not 

def isprime(n):
  if n<=1:
    return False
    print("This is not Prime")

  for i in range( 2, n):
     if i % n == 0:
      return False
     else:
       return True

n= int(input("enter your number to check prime: "))
print(isprime(n))
