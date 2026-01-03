def longest_cosecutive(nums):
    numSet=set(nums)
    longest=0
    
    for i in numSet:
        if (nums+1) not in numSet:
            lenght=1
            while (lenght+nums) in numSet:
                lenght+=1
            longest=max(lenght,longest)
    return longest
