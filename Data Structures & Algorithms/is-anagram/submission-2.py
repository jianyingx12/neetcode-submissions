class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt = {}

        for i in s:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        for x in t:
            if x in countt:
                countt[x] += 1
            else:
                countt[x] = 1
        
        return countt == counts

