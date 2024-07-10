def longestConsecutive(nums):
    sett = set(nums)
    print(sett)
    longestSub = 0
    count=0
    for i in sett:
        if i-1 not in sett:
            mini = i
            count=1
            print(i)

            while mini+1 in sett:
                mini+=1
                count+=1
            longestSub = max(longestSub,count)

    
    return longestSub

            


print(longestConsecutive([100,4,200,1,3,2,5,7,400]))
