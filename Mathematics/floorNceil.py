def floorDiv(a, b):
    
    # Python's // operator gives correct floor division
    return a // b

# Method to compute ceil of a / b
def ceilDiv(a, b):
    
    # Flip signs to force ceiling behavior
    return -(-a // b)

# Method to compute both floor and ceil of a / b
def divFloorCeil(a, b):
    res = []
    res.append(floorDiv(a, b))
    res.append(ceilDiv(a, b))
    return res

if __name__ == "__main__":
    a, b = -7, 2
    res = divFloorCeil(a, b)
    print(res[0], res[1])