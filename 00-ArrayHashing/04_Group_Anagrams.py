'''
49. Group Anagrams:
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

'''
from collections import defaultdict  

# Naive - sorting
def groupAnagrams(strs):
    res = defaultdict(list)
    
    for s in strs:
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)
        
    return list(res.values)

# Hash Table 
def groupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())