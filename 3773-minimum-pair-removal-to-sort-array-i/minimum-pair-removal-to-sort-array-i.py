class Solution:
    def minimumPairRemoval(self, nums):
        
        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        operations = 0

        while not is_sorted(nums):

            min_sum = float('inf')
            idx = 0

            # find leftmost adjacent pair with minimum sum
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]

                if pair_sum < min_sum:
                    min_sum = pair_sum
                    idx = i

            # replace pair with their sum
            nums = nums[:idx] + [min_sum] + nums[idx + 2:]

            operations += 1

        return operations        