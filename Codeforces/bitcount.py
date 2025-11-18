'''today I learn new thing which is bit_count
bit count means in a Integer howmany ones in the binary representaion of that number
the defaule function name is n.bit_count()
'''

#create bit count finding function
def bitcount(n):
  cnt=0
  while n:
    if n%2==1:
      cnt+=1
    n//=2
  return cnt
print(bitvount(5))

#calling default function
x=5
print(x.bit_count())
