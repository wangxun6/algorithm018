class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums==[]:
            return -1
        l=0
        r=len(nums)-1
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]<nums[r]:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid
            else:
                if nums[l]<=target<=nums[mid]:
                    r=mid
                else:
                    l=mid+1
        if nums[l]==target:
            return l
        else:
            return -1