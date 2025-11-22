class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = None
        missing = None
        
        for i in range(1, len(nums) + 1):
            amount = nums.count(i)

            if amount == 2:
                duplicate = i
            elif amount == 0:
                missing = i
        
        return [duplicate, missing]