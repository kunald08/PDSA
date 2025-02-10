'''
# 242. Valid Anagram:
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Input: s = "racecar", t = "carrace"
Output: true
'''

# sorting | TC: O(NlogN+MlogM), SC: O(1) or O(N+M) depending on sorting algo
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)


# Hash Table | TC: O(N+M), SC: O(1) since at most 26 diff character
def isAnagram2(s, t):
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    return countS == countT

# Hash table optimal | TC: O(N+M) SC: O(1)
def isAnagram3(s, t):
    if len(s) != len(t):
        return False
    
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
        
    for val in count:
        if val != 0:
            return False
    return True


#driver code:)
def test_isAnagram():
    test_cases = [
        ("racecar", "carrace", True),
        ("hello", "olleh", True),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "b", False),
        ("", "", True)
    ]
    
    for s, t, expected in test_cases:
        assert isAnagram(s, t) == expected, f"Failed on {s}, {t}"
        assert isAnagram2(s, t) == expected, f"Failed on {s}, {t}"
        assert isAnagram3(s, t) == expected, f"Failed on {s}, {t}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_isAnagram()