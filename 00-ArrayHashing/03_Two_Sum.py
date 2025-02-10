# 1. Two Sum:
# nums[i] + nums[j] == target and i != j.

# Naive | TC: O(n^2) SC: O(1)
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Sorting | TC: O(NlogN) SC: O(N)
def twoSum2(nums, target):
    A = []
    for i, num in enumerate(nums):
        A.append([num, i])
        
    A.sort()
    i, j = 0, len(nums)-1
    while i < j:
        cur = A[i][0] + A[j][0]
        if cur == target:
            return [min(A[i][1], A[j][1]),
                    max(A[i][1], A[j][1])]
        elif cur < target:
            i += 1
        else:
            j -= 1
    return []

# Hash Map (Two pass) | TC: O(n) SC: O(n)
def twoSum3(nums, target):
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        
# Hash Map (one pass) | TC: O(n) SC: O(n)
def twoSum4(nums, target):
    prevMap = {}  # val -> index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

        
        
def test_twoSum():
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        # ([1, 2, 3, 4], 8, []), assumtion so that
        ([0, 4, 3, 0], 0, [0, 3])
    ]
    
    for nums, target, expected in test_cases:
        assert twoSum(nums, target) == expected, f"Failed on {nums}, {target}"
        assert twoSum2(nums, target) == expected, f"Failed on {nums}, {target}"
        assert twoSum3(nums, target) == expected, f"Failed on {nums}, {target}"
        assert twoSum4(nums, target) == expected, f"Failed on {nums}, {target}"
    
    print("All Two Sum test cases passed!")

if __name__ == "__main__":
    test_twoSum()
