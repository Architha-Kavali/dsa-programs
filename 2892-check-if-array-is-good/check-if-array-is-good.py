class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=max(nums)
        expected=list(range(1,n+1))
        expected.append(n)
        nums.sort()
        return expected==nums
        