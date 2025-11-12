'''https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/'''
#Approch
#1. first has to find if there any ones exists in the given list if it is return different length of list between number os ones.
#2. if there no ones in the given list the find if it is possible to get 1 as return of two next numbers GCD if it is manipulating list times + length of intial list


"""My Code"""
class Solution:
    def gcd(a,b):
        return a if b==0 else gcd(b,a%b)
    def minOperations(self, nums: List[int]) -> int:
        a=1
        if a in set(nums):
            ones=0
            for i in nums:
                if i==1:
                    ones+=1
            return len(nums)-ones
        cnt=len(nums)
        n=len(nums)
        while True:
            lst=[]
            for i in range(n-1):
                x=gcd(nums[i],nums[i+1])
                if x==1:
                    return cnt
                lst.append(x)
            lst.append(lst[-1])
            if len(set(lst))==1 or lst==nums:
                break
            nums[:]=lst
            cnt+=1
        return -1
