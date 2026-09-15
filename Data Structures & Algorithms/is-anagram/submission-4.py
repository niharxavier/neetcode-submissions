class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charCount1 = dict()
        charCount2 = dict()
        for char in s:
            if char in charCount1.keys():
                charCount1[char] += 1
            else:
                charCount1[char] = 1
        for char in t:
            if char in charCount2.keys():
                charCount2[char] += 1
            else:
                charCount2[char] = 1
        
        if charCount1 == charCount2:
            return True
        return False