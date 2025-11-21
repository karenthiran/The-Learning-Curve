'''https://www.geeksforgeeks.org/problems/lucky-numbers2911/0'''

#code
class Solution:
    def isLucky(self, n): 
        
        if n%2==0:
            return 0
        if n==1:
            return 1
        i=2
        while i<n+1:
            if n%i==0:
                return 0
            n=(n-(n//i))
            i+=1
        return 1
