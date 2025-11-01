# shuffle the array
def shuffleArr(nums, n): # n --> len(nums)//2
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
        
    return ans # TC: O(n) | SC: O(n)


def shuffle(nums, n):
    
    # Step 1: Encode both nums[i] and nums[i+n] into nums[i]
    for i in range(n):
        xi = nums[i]
        yi = nums[i + n]
        nums[i] = xi + yi * 10000  # Combine y and x into one number

    # Step 2: Decode them back into correct order, starting from back
    for i in range(n - 1, -1, -1):
        combined = nums[i]
        xi = combined % 10000       # Get original xi (remainder)
        yi = combined // 10000      # Get original yi (quotient)
        nums[2 * i] = xi
        nums[2 * i + 1] = yi

    return nums   # TC: O(n) | SC: O(1)
