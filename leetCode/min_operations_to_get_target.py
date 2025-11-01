"""
Problem: [0,0,0,0] -> [1,3,2,1]  -> o/p --> 3
you can add 1 in any subarray for the 1 operation

"""


def minNumberOperations(target):
    res = prev = 0
    for n in target:
        if n > prev:
            res += (n-prev)
        prev = n
    return res
    
    
target = [1,4,3,2,4]
target = [1,2,3,2,1]
target = [1,2,3,2,1,2,3]

print(minNumberOperations(target))