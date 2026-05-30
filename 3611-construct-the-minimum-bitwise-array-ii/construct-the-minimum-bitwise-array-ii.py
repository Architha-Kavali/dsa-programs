class Solution:
    def minBitwiseArray(self, nums):
        ans = []

        for x in nums:
            if x == 2:
                ans.append(-1)
                continue

            d = 1
            res = x

            while x & d:
                res = x - d
                d <<= 1

            ans.append(res)

        return ans