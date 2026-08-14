## function to find the greatest element 


def greatest(num):
  max= num[0]
  for i in range(len(num)):
    if num[i] > max:
      max= num[i]
  return max

num= [12,4,5,77,88,4,5]
print(greatest(num))
