class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        def dfs(nums, temp_list):
            if len(temp_list) == n:
                res.append(temp_list)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i]+nums[i+1:], temp_list+[nums[i]])
        res = []
        n = len(nums)
        nums.sort()
        dfs(nums, [])
        return res