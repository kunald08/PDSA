# Problem 217: Given an integer array nums, return true if any value appears more than once in the array,
#              otherwise return false.

# Naive Approach: Compare each element with every other element
# TC: O(N^2) | SC: O(1)
def hasDuplicates(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Sorting Approach: Sort the array and check for adjacent duplicates
# TC: O(N log N) | SC: O(1) or O(N) depending on sorting algorithm

def hasDuplicates2(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

# Hash Set Approach: Store elements in a set and check for duplicates
# TC: O(N) | SC: O(N)
def hasDuplicates3(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Hash Set Length Approach: Convert list to set and compare lengths
# TC: O(N) | SC: O(N)
def hasDuplicates4(nums):
    return len(set(nums)) < len(nums)

# Taking input from the user
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Checking for duplicates using different approaches
print(f"Naive Approach: {hasDuplicates(nums)}")
print(f"Sorting Approach: {hasDuplicates2(nums)}")
print(f"Hash Set Approach: {hasDuplicates3(nums)}")
print(f"Set Length Approach: {hasDuplicates4(nums)}")