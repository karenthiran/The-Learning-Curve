'''https://www.geeksforgeeks.org/problems/stack-permutations/1?page=4&difficulty=Medium&status=unsolved&sortBy=accuracy'''
#Explanation
'''https://www.geeksforgeeks.org/stack-permutations-check-if-an-array-is-stack-permutation-of-other/'''
#code
class Solution:
    def validateOp(self, a, b):
        lst=[]
        j=0
        for i in a:
            lst.append(i)
            while len(lst)!=0 and lst[-1]==b[j]:
                lst.pop()
                j+=1
        return len(lst)==0
