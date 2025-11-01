# two pass search
def getSecondHighest(nums):
    large = float('-inf')
    for n in nums:
        if n > large:
            large = n
    
    s_large = float('-inf')
    for n in nums:
        if n > s_large and n != large:
            s_large = n
    
    return [s_large if s_large != float('-inf') else -1, large]

# One pass search
def getSecondHighest2(nums):
    if len(nums) < 2:
        return -1
    
    large, s_large = float('-inf'), float('-inf')
    
    for n in nums:
        if n > large:
            s_large = large
            large = n
        elif n > s_large and n != large:
            s_large = n
    return s_large if s_large != float('-inf') else -1





nums = [10, 20, 40, 22, 44, 37, 7, 47, 37]
print(getSecondHighest2(nums))