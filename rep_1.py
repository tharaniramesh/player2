# thara
import collections
n=int(input())
a=list(map(int,input().split()))
fre=collections.Counter(a)
c=0
for x,y in fre.items():
      if y==1:
            if c==0:
                  print(x,end="")
                  c+=1
            else:
                   print("",x,end="")
