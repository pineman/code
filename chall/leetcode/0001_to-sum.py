class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    #    n = len(nums)
    #    for i in range(n):
    #        for j in range(i, n):
    #            if nums[i] + nums[j] == target:
    #                if i == j: continue
    #                return [i, j]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, n in enumerate(nums):
            r = target - n
            if r in s:
                return [i, s[r]]
            s[n] = i
        return []
