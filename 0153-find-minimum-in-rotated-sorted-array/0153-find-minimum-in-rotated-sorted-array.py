class Solution:
    def findMin(self, nums: list[int]) -> int:
        low=0
        high=len(nums)-1
        res=5001
        while low<=high:
            mid=int((low+high)/2)
            if nums[mid]>=nums[low]:
                res=min(res,nums[low])
                low=mid+1
            else :
                res=min(res,nums[mid])
                high=mid-1
        return res
