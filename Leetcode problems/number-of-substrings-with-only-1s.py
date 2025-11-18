'''https://leetcode.com/problems/number-of-substrings-with-only-1s/?envType=daily-question&envId=2025-11-16'''

#code
class Solution:
    def numSub(self, s: str) -> int:
        mod=1000000007
        ans=0
        prv='0'
        cnt=1
        for i in s:
            if prv=='1' and i=='1':
                cnt+=1
            elif prv=='1' and i=='0':
                cnt=(cnt+1)*cnt
                cnt=cnt//2
                ans+=cnt
                cnt=1
                ans=ans%mod
            prv=i
        if prv=='1':
            cnt=(cnt+1)*cnt
            cnt=cnt//2
            ans+=cnt
            ans=ans%mod 
        return ans
