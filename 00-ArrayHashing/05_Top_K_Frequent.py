# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# Naive | TC: O(n^2)
def topKFrequent(nums,k):
    ans = []
        
    for i in range(len(nums)):
        cnt = 1
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                cnt += 1
        if cnt >= k and nums[i] not in ans:  # Added condition to check if element is already in ans
            ans.append(nums[i])
    return ans

# sorting
def topKFrequent2(nums, k):
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    
    arr = []
    for num,  cnt in count.items():
        arr.append([cnt, num])
    arr.sort()
    
    res = []
    while len(res) < k:
        res.append(arr.pop()[1])
    return res
 
# Using Heap | TC: O(n), SC: O(n)    
import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)  # Count the frequency of each element
    return heapq.nlargest(k, count.keys(), key=count.get)  # Get the k most frequent elements
   
    
    

nums = [1,2,2,3,3,3]
k = 2                
print(topKFrequent2(nums, k))     
        
    