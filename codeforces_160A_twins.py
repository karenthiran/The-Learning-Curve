'''The "Twins" question (Codeforces 160A) was one of the first problems I encountered when I started doing Codeforces, and I couldn't solve it. I couldn't even understand the 
question at the time. However, after a couple of years, I solved the same problem within 15 minutes.I achieved this only through consistent work on learning to code—not just by 
watching YouTube tutorials but by actively practicing them. Now, I can find several patterns in some complicated questions. Here is my optimal solution for this question.'''

# my code
n=int(input())
lst=list(map(int,input().split()))
lsum=sum(lst)
lst.sort()
lst=lst[::-1]
ans=0
ihave=0
for i in lst:
    ihave+=i
    lsum-=i
    ans+=1
    if ihave>lsum:
        break;
print(ans)
