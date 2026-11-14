class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid_index = (start + end) // 2
            if nums[mid_index] == target:
                return mid_index
            elif target > nums[mid_index]:
                start = mid_index + 1
            else:
                end = mid_index - 1
        return -1
        
        