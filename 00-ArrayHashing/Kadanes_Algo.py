# find a not-empty subarray with the largest sum.

# Brute Force: O(n^2)
def bruteForce(nums):
    maxSum = nums[0]  # float('-inf') 

    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum

def kananes(nums):
    maxSum = nums[0]  # float('-inf') 
    curSum = 0
    
    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum  

# Return the left and right index of the max subarray sum,
# assuming there's exactly one result (no ties).
# Sliding window variation of Kadane's: O(n)
def slidingWindow(nums):
    maxSum = nums[0]  # float('-inf') 
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            L = R

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R 

    return [maxL, maxR]


nums = [4, -1, 2, -7, 3, 4]  # [3, 4] --> 7
print(bruteForce(nums))