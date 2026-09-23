class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""

        i = 0

        while True:

            if i >= len(strs[0]):
                break

            char = strs[0][i]

            for w in strs:
                if i >= len(w) or w[i] != char:
                    return pre

            pre += char
            i += 1
        return pre
