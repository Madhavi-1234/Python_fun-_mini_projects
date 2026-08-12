### patterns printng

def pattern(n):
  # base condition
  if(n==0):
    return
  print( '*' * n)
  pattern(n-1)

n= int(input("Enter the value for n :"))
pattern(n)
