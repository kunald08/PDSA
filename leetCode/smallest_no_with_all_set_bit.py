# Problem: Smallest no with all set bit --> >=
# 1, 3, 7, 15, 31,...

def smallestNumber(n):  
    x = 1
    while x < n:
        x = x*2 +1
    return x

def smallestNumber2(n):
    res = 1
    
    while res < n:
        res = (res << 1) | 1
    return res
    
    
    
n = 8
# print(smallestNumber(n))
# print(smallestNumber2(n))

