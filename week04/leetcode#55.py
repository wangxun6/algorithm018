class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = 0
        for i,jump in enumerate(nums):
            if length >= i and i +jump > length:
                length = i +jump
        return length >= i
