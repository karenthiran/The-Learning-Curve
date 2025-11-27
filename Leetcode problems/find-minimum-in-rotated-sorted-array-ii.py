'''https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/'''

#code
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left<right:
            mid = (left+right)//2

            if nums[mid]>nums[right]:
                # not sorted
                left=mid+1
            
            elif nums[mid]<nums[right]:
                right = mid
            else:
                #dont know what to do.
                right-=1
        return nums[right]
