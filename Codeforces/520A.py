# https://codeforces.com/problemset/problem/520/A
'''In my day-to-day life, I feel like my problem-solving skills and logical thinking are getting better every day. Today, I solved the Codeforces question (520A) - "Pangram," 
which is an easy question now, but four years ago I couldn't have solved it. This brings me to my point. First, I solved it the usual way. After a minute of thinking, 
I got another good idea. After implementing the second idea, I came up with a way to write the code in a single line. This made me happy and gave me more energy to stay consistent. 
Here are my three solutions.'''

# Solution 1: using ASCII
n=int(input())
s=input()
if n<26:
    print('NO')
else:
    s=s.lower()
    flag=True
    for i in range(97,123):
        if chr(i) not in s:
            print('NO')
            flag=False
            break
    if flag:
        print('YES')

# Solution 2: using set data structure
input()
s=input()
s=s.lower()
st=set(s)
if len(st)==26:
    print('YES')
else:
    print('NO')

# Solution 3: Implement nd idea in single line
input();print( 'YES' if len(set(input().lower()))==26 else 'NO')
