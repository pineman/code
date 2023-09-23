class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        # Ver notebook novabase
        def f(nums):
            if len(nums) < 3:
                return 1
            root = nums[0]
            left = [i for i in nums if i < root]
            right = [i for i in nums if i > root]
            return f(left) * f(right) * math.comb(len(nums)-1, len(left))
        return (f(nums)-1) % (10**9+7)
