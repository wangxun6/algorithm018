class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}
        for i, value in enumerate(nums):
            hash1[value] = i

        for i, value in enumerate(nums):
            j = hash1.get(target - value)
            if j is not None and i != j:
                return [i, j]
