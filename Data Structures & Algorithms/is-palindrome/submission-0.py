import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        #print("s:", s)
        l = int(len(s)/2)
        for i in range(l):
            if s[i] != s[len(s) - i - 1]:
                return False
            i+=1
        return True
        