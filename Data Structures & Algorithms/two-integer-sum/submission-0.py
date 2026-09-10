class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matching_num_idx_map = {}
        for i, num in enumerate(nums):
            if num in matching_num_idx_map:
                return [matching_num_idx_map[num], i]
            else:
                matching_num_idx_map[target-num] = i
        