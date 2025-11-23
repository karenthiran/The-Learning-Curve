'''https://www.geeksforgeeks.org/problems/largest-prime-factor2601/0'''
#code
class Solution:
    def largestPrimeFactor(self, n):
        def isPrime(n):
            if n==2:
                return True
            i=2
            while i*i<=n:
                if n%i==0:
                    return False
                i+=1
            return True
        
        if isPrime(n):
            return n
        maxPrime=-1
        i=2
        while i*i<=n:
            if n%i==0:
                x=n//i
                if isPrime(x):
                    return x
                if isPrime(i):
                    maxPrime=i
            i+=1
        return maxPrime
        
