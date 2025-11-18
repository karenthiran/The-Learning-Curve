'''https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/1830181344/'''

'''code'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans=[]
        n=len(words[0])
        m=len(words)
        l=len(s)
        x=0
        d={}
        for i in words:
            d[i]=d.get(i,0)+1
        dc=d.copy()
        for i in range(l-n*m+1):
            st=s[i:i+n]
            if st in dc and dc[st]>0:
                x=1
                dc[st]=dc[st]-1
                j=i+n
                while x<m and j<=l-n:
                    st=s[j:j+n]
                    if st in dc and dc[st]>0:
                        x+=1
                        dc[st]=dc[st]-1
                    else:
                        break
                    j+=n
                dc=d.copy()
            if x==m:
                ans.append(i)
                dc=d.copy()
                x=0
        return ans
            
            
