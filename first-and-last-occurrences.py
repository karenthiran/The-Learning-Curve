'''https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/0'''

#code
class Solution:
    def find(self, arr, x):
        first,last=-1,-1
        i,j=0,len(arr)-1
        while i<=j:
            mid=(i+j)//2
            if mid>0 and arr[mid]==x and arr[mid-1]<x:
                first=mid
                break
            elif mid==0 and arr[mid]==x:
                first=mid
                break
            elif arr[mid]==x and arr[mid-1]==x:
                j=mid-1
            elif arr[mid]>x:
                j=mid-1
            elif arr[mid]<x:
                i=mid+1
        i,j=0,len(arr)-1
        while i<=j:
            mid=(i+j)//2
            if mid<len(arr)-1 and arr[mid]==x and arr[mid+1]>x:
                last=mid
                break
            elif mid==len(arr)-1 and arr[mid]==x:
                last=mid
                break
            elif arr[mid]==x and arr[mid+1]==x:
                i=mid+1
            elif arr[mid]>x:
                j=mid-1
            elif arr[mid]<x:
                i=mid+1
        return [first,last]
