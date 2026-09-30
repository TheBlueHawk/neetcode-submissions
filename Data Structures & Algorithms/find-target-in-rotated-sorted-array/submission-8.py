class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            print(nums[l],nums[mid],nums[r])
            # found it
            if nums[mid] == target:
                return mid
            # we're in the sorted part
            elif nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            # rotated
            else:
                # rotation second half
                if nums[mid] > nums[r]:
                    print("rot-2")
                    if target > nums[mid] or target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
                # rotations first half
                else:
                    print("rot-1")
                    if target > nums[r] or target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
        return -1