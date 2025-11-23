'''https://codeforces.com/problemset/problem/1878/C'''

#code
t=int(input())
for _ in range(t):
    n,k,x=map(int,input().split())
    a=(n*(n+1))//2
    if a<x:
        print('NO')
        continue
    minval=(k*(k+1))//2
    n-=k
    maxval=(n*(n+1))//2
    maxval=a-maxval
    if minval<=x and x<=maxval:
        print('YES')
    else:
        print('NO')
