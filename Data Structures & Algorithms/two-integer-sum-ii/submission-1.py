class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1
        while l < r:
            sum2 = numbers[l] + numbers[r]
            if sum2 == target:
                return [l+1, r+1]
            if sum2 > target:
                r -= 1
            else:
                l +=1
