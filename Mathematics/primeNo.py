# A prime number -> is a natural no > 1
#                -> and has exactly 2 divisor, 1 and itself

import math

def isPrime(n):
    #check if n is 1 or 0
    if n <= 1:
        return False
    
    #check if n is 2 or 3
    if n == 2 or n == 3:
        return True
    
    #check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    #check from 5 to square root of n
    #iterate i by (i+6)
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
        
    return True


if __name__ == "__main__":
    n = 7
    if isPrime(n):
        print("true")
    else:
        print("false")    