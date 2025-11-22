class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = range(len(nums))
        for i in length:
            for j in length:
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    return [i, j]