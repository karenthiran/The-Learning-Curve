'''https://leetcode.com/problems/smallest-integer-divisible-by-k/?envType=daily-question&envId=2025-11-25'''

#code
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0:
            return -1
        if k==1:
            return 1
        n=1
        l=1
        while n%k!=0:
            n=n*10+1
            l+=1
        return l
