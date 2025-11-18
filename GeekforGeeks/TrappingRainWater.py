'''https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article'''

#Code

class Solution:
    def maxWater(self, arr):
        ans=0
        res=0
        n=len(arr)
        if n<=2:
            return 0 
        prv=arr[-1]
        l=n-1
        for i in range(n-2,0,-1):
            if arr[i]>=prv:
                x=l-i-1
                x=x*(prv)
                ans+=x
                prv,l=arr[i],i
                res=ans
            else:
                ans-=arr[i]
        if arr[0]>=prv:
            x=l-1
            x=x*(prv)
            ans+=x
            return ans
        ans=0
        prv=arr[0]
        m=0
        for i in range(1,l+1):
            if prv<=arr[i]:
                x=i-m-1
                x=x*prv
                ans+=x
                prv,m=arr[i],i
            else:
                ans-=arr[i]
        return res+ans
