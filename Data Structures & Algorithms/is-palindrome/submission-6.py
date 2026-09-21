class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for char in range(len(s)):
            if s[char].isalnum():
                clean += s[char].lower()

        print(clean, clean[::-1])

        return clean == clean[::-1]