class Solution(object):
    def minBitFlips(self, start, goal):
        bit=start^goal
        count=0
        for i in range(32):
            if bit&(1<<i):
                count+=1
        return count
        