class Solution:
    def ValidPair(self, l, r):
        return ((l=='(' and r==')') or (l=='{' and r=='}') or (l=='[' and r==']'))

    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                #print("opening bracket")
                stack.append(s[i])
                #print(stack[-1])
            elif len(stack)==0 or not self.ValidPair(stack[-1], s[i]):
                return False
            else:
                stack.pop()
        if not stack:
            return True
        return False
            
            