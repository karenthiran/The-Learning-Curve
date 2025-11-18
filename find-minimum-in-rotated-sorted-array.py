'''https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1833190557/?envType=problem-list-v2&envId=binary-search'''

#mycode
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if nums[0]<nums[-1]:
            return nums[0]
        if nums[-1]<nums[-2]:
            return nums[-1]
        i,j=0,len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                return nums[mid]
            elif nums[mid]>nums[j]:
                i=mid+1
            else:
                j=mid-1
        return -1
