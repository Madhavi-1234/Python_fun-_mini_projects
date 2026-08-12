## greatest among three numbers 

def greatest(n1, n2, n3):
  if (n1>n2 and n1>n3):
    return n1
  elif( n2> n1 and n2> n3):
   return n2
  else:
    return n3

a= int(input("Enter the number:"))
b= int(input("Enter the number:"))
c= int(input("Enter the number:"))

print(f" greatest of all your three numbers is : {greatest(a,b,c)}")
