'''in a given sorted array find the first occurance of the given element. the array can contains duplicate elements. 
here  is the problem link https://www.geeksforgeeks.org/problems/binary-search-1587115620/1?page=1&sortBy=submissions 
'''
#Optimal Solution
class Solution:
    def binarysearch(self, arr, k):
        if arr[len(arr)-1]<k:
            return -1
        i,j=0,len(arr)-1
        while i<=j:
            mid=(i+j)//2
            if mid==0 and arr[mid]==k:
                return mid
            elif mid>0 and arr[mid]==k and arr[mid-1]!=k:
                return mid
            elif mid>=0 and arr[mid]==k and arr[mid-1]==k:
                j=mid-1
            elif arr[mid]>k:
                j=mid-1
            elif arr[mid]<k:
                i=mid+1
        return -1
            
        
