class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=int((low+high)/2)
            if nums[mid]==target:
                return True
            elif nums[low]==nums[mid] and nums[mid]==nums[high]:
                low+=1
                high-=1
            elif nums[low]>nums[mid]:
                if nums[mid]<target and target<=nums[high]:
                    low+=1
                else:
                    high-=1
            else:
                if nums[low]<=target and target<nums[mid]:
                    high-=1
                else:
                    low+=1
        return False