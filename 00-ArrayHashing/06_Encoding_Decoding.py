# Design an algorithm to encode a list of strings to a single string. 
# The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# 
def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(s):
    res = []
    i = 0
    
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j
        
    return res