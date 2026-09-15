class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sDict = dict()
        tDict = dict()

        for x in s:
            if x not in sDict.keys():
                sDict[x] = 1
            else:
                sDict[x] += 1
        for x in t:
            if x not in tDict.keys():
                tDict[x] = 1
            else:
                tDict[x] += 1
        
        if sDict == tDict:
            return True
        
        return False