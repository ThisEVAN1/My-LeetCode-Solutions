class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half = [nums[i] for i in range(n)]
        second_half = [nums[i + n] for i in range(n)]

        finished_list = []
        for i in range(n):
            finished_list.append(first_half[i])
            finished_list.append(second_half[i])
        
        return finished_list