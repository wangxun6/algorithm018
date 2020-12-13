class Solution:
    def reverseBits(self, n: int) -> int:
        ans ,mark = 0 ,1
        for i in range(32):
            if n & mark:
                ans |= 1 << (31-i)
            mark <<=  1
        return ans