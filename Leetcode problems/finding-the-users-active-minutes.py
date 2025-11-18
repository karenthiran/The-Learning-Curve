'''Today I learned a new thing in hashtable which means in dictionary can create a default dictionary like d=defaultdict(set)'''
#d=defaultdict(set)

#mycode
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d={}
        for i in logs:
            x,y=i[0],i[1]
            if x not in d:
                st=set()
                st.add(y)
                d[x]=st
            else:
                st=d[x]
                st.add(y)
                d[x]=st
        lst=[0]*k
        for k,v in d.items():
            x=len(v)
            lst[x-1]=lst[x-1]+1
        return lst

#top User code
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d=defaultdict(set)
        for i,j in logs:
            d[i].add(j)
        res=[0]*k
        for i in d.values():
            j=len(i)
            if j<=k:
                res[j-1]+=1
        return res
