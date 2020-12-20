class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash1 = {}
        for i in s:
            if i not in hash1:
                hash1[i] = 1
            else:
                hash1[i] += 1
        for key in hash1.keys():
            if hash1[key] == 1:
                return s.find(key)
        return -1