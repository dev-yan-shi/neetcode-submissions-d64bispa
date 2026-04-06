class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,res = 0,0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            print("charSet before update", charSet)
            res = max(res, len(charSet))
        return res