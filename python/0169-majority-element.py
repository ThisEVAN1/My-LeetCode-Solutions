class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        for num in nums:
            try:
                majority[num] += 1
            except KeyError:
                majority[num] = 0

        majority_num = ['key', -999]
        for key, value in majority.items():
            if value > majority_num[1]:
                majority_num[0] = key
                majority_num[1] = value

        return majority_num[0]