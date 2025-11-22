class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        max_consecutive = 0
        for i in nums:
            if i:
                consecutive += 1
                max_consecutive = max(consecutive, max_consecutive)
            else:
                consecutive = 0

        return max_consecutive