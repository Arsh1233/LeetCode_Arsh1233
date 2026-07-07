class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        zcnt=0
        pro=1
        for i in range(len(nums)):
            if nums[i]!=0:
                pro*=nums[i]
            else:
                zcnt+=1
        if zcnt>1:
            return [0]*len(nums)
        for i in range(len(nums)):
            if zcnt==1:
                if nums[i]==0:
                    ans[i]=pro
                else:
                    ans[i]=0
            else:
                ans[i]=pro//nums[i]
        return ans
