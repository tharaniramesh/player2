k=int(input())
a=[]
for i in range(0,k):
      a.append(list(map(int,input().split())))
b=sorted(a)
v=[]
for i in b:
      for j in i:
            v.append(j)
d=sorted(v)
print(*d)
