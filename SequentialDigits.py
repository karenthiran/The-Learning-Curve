'''https://leetcode.com/problems/sequential-digits/'''

#code
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n=len(str(low))
        x=int(str(low)[0])
        num=x
        for i in range(n-1):
            num=num*10+(x+1)
            x+=1
        isseq=True
        s=str(num)
        for i in range(1,n):
            if int(s[i])!=int(s[i-1])+1:
                isseq=False
                break
        if not isseq:
            n+=1
            num=0
            for i in range(n):
                num=num*10+i
        lst=[]
        while num<=high:
            lst.append(num)
            s=str(num)
            if s[-1]!='9':
                s=s[1:]
                num=int(s)
                num=(num*10)+((num%10)+1)
            else:
                x=1
                for i in range(2,len(s)+2):
                    x=x*10+(i)
                num=x
        while len(lst)!=0 and lst[0]<low:
            lst.pop(0)
        return lst

