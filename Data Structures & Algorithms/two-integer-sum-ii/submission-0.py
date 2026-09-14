class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        matches = {}
        for i, num in enumerate(numbers):
            if num in matches:
                return [matches[num], i +1]
            else:
                matches[target-num] = i+1