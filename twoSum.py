# Brute force
# it is simple running the loop and finding the best possible pair
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


# HashMap
# Using hashmap you store the num that's complement with target is not in 
# hashmap and if you encounter its complement in the hashmap you return the 
# num in hashmap and the complement
def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return None


# Two pointer approach
# Sort the array and keep track of the original indices.
# Initialize two pointers, one at the beginning and one at the end of the array.
# While the pointers don't cross each other:
# If the sum of the elements at the pointers equals the target, return their indices.
# If the sum is less than the target, move the left pointer to the right.
# If the sum is greater than the target, move the right pointer to the left.

def twoSum(nums, target):
    sorted_nums = sorted((num, i) for i, num in enumerate(nums))
    left, right = 0, len(nums) - 1
    while left < right:
        sum = sorted_nums[left][0] + sorted_nums[right][0]
        if sum == target:
            return [sorted_nums[left][1], sorted_nums[right][1]]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return None


# Using SET
# Create an empty set.
# Loop through the array.
# For each element, check if the complement (target - element) is in the set.
# If it is, return the pair.
# Otherwise, add the element to the set.

def twoSum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return [num, complement]
        seen.add(num)
    return None
