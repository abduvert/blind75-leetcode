def containsDuplicate(nums):
    nums.sort()
    print(nums)
    for i in range(len(nums)):
        if(i!=len(nums)-1):
            if(nums[i]==nums[i+1]):
                return True
    return False





print(containsDuplicate([0,4,5,1,6,6]))