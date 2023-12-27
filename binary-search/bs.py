from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1
        while start <= end:
            mid = start + (end -  start)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return  -1
            

s= Solution()
assert s.search([-1,0,3,5,9,12], 13) == -1