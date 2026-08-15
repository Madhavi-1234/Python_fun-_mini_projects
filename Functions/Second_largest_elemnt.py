## second Largest Element

def secondlargest(num):
  largest= num[0]
  second= None
  for i in range(len(num)):
    if num[i]> largest:
      largest= num[i]
  for i in range(len(num)):
    if num[i]< largest:
      if second is None or num[i]>second:
       second= num[i]
  return second

num= [1,44,5,66,3,44,88,9]
print(secondlargest(num))
