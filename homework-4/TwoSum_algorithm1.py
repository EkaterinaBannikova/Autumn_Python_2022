class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                if nums[i1] + nums[i2] == target:
                    return [i1, i2]
