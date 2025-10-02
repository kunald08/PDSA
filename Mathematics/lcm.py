def lcm(a, b):
    
    # Larger value
    g = max(a, b) 
    
    # Smaller value
    s = min(a, b)  

    for i in range(g, a * b + 1, g):
        if i % s == 0:
            return i
    return a * b 

#########################################################
# function for gcd
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm2(a, b):
    return (a // gcd(a, b)) * b


# main
if __name__ == '__main__':
    a = 10
    b = 5
    print(lcm(a, b))