n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,len(a)):
    if i==a[i]:
        b.append(a[i])
c=sorted(b)
print(*c)
