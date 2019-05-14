n,k=map(int,input().split())
a=list(map(int,input().split()))
b=sorted(a,reverse=True)
c=b[k-1]
print(c)
