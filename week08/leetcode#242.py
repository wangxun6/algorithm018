class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hash1 = {}
        # if len(s) != len(t):
        #     return False
        # for i in s:
        #     if i not in hash1:
        #         hash1[i] = 1
        #     else:
        #         hash1[i] += 1
        # for i in t:
        #     if i not in hash1:
        #         return False
        #     if i in hash1:
        #         hash1[i] -= 1
        # for value in hash1.values():
        #     if value != 0:
        #         return False
        # return True
        if sorted(s) == sorted(t):
            return True
        else:
            return False
