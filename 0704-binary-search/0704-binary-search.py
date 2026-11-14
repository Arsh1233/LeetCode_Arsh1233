class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=int((low+high)/2)
            if nums[mid]==target:
                print(mid)
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1