class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = {nums[0]: 0}
        for i in range(1, len(nums)):
            d = target - nums[i]
            if d in dicti:
                return [dicti[d], i]
            dicti[nums[i]] = i
            