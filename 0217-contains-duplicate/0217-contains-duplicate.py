class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        res=set()
        for i in nums:
            if i in res:
                return True
            res.add(i)
        return False