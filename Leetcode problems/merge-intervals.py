'''https://leetcode.com/problems/merge-intervals/'''

#code
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        lst=[]
        start,end=None,0
        n=0
        for i in intervals:
            n=max(n,i[1])
            if start==None:
                start,end=i[0],i[1]
            else:
                if end<i[0]:
                    l=[start,end]
                    lst.append(l)
                    start,end=i[0],i[1]
                if end<i[1]:
                    end=i[1]
        l=[start,n]
        lst.append(l)
        return lst
            
