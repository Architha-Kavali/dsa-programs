class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        ans=[]
        for x in nums:
            found=-1
            for a in range(x):
                if (a|(a+1))==x:
                    found=a
                    break
            ans.append(found)
        return ans
        