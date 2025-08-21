'''Today I solved codeforeces couple of question. I quiet like the question today (144A) Arrival of the General. when i solve this question I learned new things in pyhton 
1. del in list 
   lst=[2,4,5,6]
   del lst[2] delete the sencond index element
2. insert in list
   lst.insert(position,value) '''

n=int(input())
lst=list(map(int,input().split()))
me=lst[0]
mp=0
mne=lst[0]
mnp=0
for i in range(1,n):
    if me<lst[i]:
        me=lst[i]
        mp=i
    if mne>=lst[i]:
        mne=lst[i]
        mnp=i
if mp>mnp:
    mnp+=1
mnp=n-mnp-1
print(mp+mnp)
