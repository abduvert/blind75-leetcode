# Write a function to return the sum of the numbers in the given array 'nums', except ignore sections of numbers starting with a 7 and extending to the next 8 (every 7 will be followed by at least one 8). 
# Return 0 for no numbers.

# sum78([1, 2, 2]) → 5
# sum78([1, 2, 2, 7, 99, 99, 8]) → 5
# sum78([1, 1, 7, 8, 2]) → 4

def sum78(nums):
  summ = 0
  inSection = False
  for i in nums:
    if i==7:
        inSection = True
    elif i==8 and inSection:
        inSection = False
    elif not inSection:
        summ += i
  return summ


print(sum78([7,1,8,6,7,3,8,5]))