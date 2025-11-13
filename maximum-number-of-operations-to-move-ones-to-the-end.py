'''https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/?envType=daily-question&envId=2025-11-13'''
#code
def maxOperations(self, s: str) -> int:
        cnt=0
        i=0
        n=len(s)
        ones=0
        while i<n:
            if s[i]=='1':
                ones+=1
            elif i>0 and s[i-1]=='1':
                cnt+=ones
            i+=1
        return cnt
