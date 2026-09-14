class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outputs = set()
        for i, target in enumerate(nums):
            _nums = nums[:i] + nums[i+1:]
            res = self.twoSum(_nums, -target)
            for r in res:
                outputs.add(tuple(sorted((target,r[0], r[1]))))
        return [list(o) for o in outputs]

        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        matches = {}
        solutions = []
        for num in numbers:
            if num in matches:
                solutions.append((matches[num],num))
            else:
                matches[target-num] = num
        return solutions