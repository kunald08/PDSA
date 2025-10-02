def gcd(a, b):
    #find minimum of a and b
    res = min(a, b)
    
    while res > 0:
        if a % res == 0 and b % res == 0:
            break
        res -= 1
        
    return res  # TC: O(min(a, b)) | SC: O(1)


def gcd2(a, b):
    # Everything divides 0
    if a == 0:
        return b
    if b == 0:
        return a

    # Base case
    if a == b:
        return a
    
    # a is greater
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


def gcd3(a, b):
    return a if b == 0 else gcd(b, a%b)


if __name__ == "__main__":
    a = 20
    b = 28
    print(gcd(a, b))