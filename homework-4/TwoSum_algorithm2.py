import operator

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        sortednums = sorted(enumerate(nums), key=operator.itemgetter(1))
        for i in range(n):
            d = target - sortednums[i][1]
            left = i + 1
            right = n - 1
            while left <= right:
                middle = (left + right) // 2
                if sortednums[middle][1] == d:
                    return [sortednums[i][0], sortednums[middle][0]]
                else:
                    if d < sortednums[middle][1]:
                        right = middle - 1
                    else:
                        left = middle + 1
