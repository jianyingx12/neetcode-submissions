class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            if char in pairs:
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[char]:
                    return False
        return not stack
            

            
                

