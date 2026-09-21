class Solution:
    def isValid(self, s: str) -> bool:
        # Map opening brackets to their corresponding closing brackets
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for x in s:
            # 1. If it's an opening bracket, push it to the stack
            if x in d:
                stack.append(x)
            # 2. If it's a closing bracket
            else:
                # If stack is empty or the top doesn't match, it's invalid
                if not stack or d[stack.pop()] != x:
                    return False
        
        # 3. If the stack is empty, all brackets were matched perfectly
        return len(stack) == 0