# alletcode question(763) partiation the string using two pointers and hashtable
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lst=[]
        pos={}
        maxpos=0
        for i in range(len(s)):
            pos[s[i]]=i
        start=0
        for i in range(len(s)):
            x=pos[s[i]]
            maxpos=max(maxpos,x)
            if i==maxpos:
                lst.append(s[start:maxpos+1])
                start=maxpos+1
        ans=[]
        for i in lst:
            ans.append(len(i))
        return ans
