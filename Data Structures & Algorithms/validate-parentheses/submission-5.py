class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for x in s:
            if x in "[({":
                stack.append(x)
            else:
                if not stack or d[stack.pop()] != x:
                    return False
        
        return len(stack) == 0