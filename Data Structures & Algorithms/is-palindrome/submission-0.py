class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ""
        for c in s.lower():
            cleanStr += c if c.isalnum() else ""
        cleanStr = "".join(cleanStr.strip())
        left, right = 0, len(cleanStr) - 1
        while left < right:
            if cleanStr[left] != cleanStr[right]:
                return False
            left += 1
            right -= 1
        return True