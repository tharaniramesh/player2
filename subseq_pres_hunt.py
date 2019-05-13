n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0

if len(b)>len(a):
    print("NO")
else:
    for i in b:
        if i in a:
            c=c+1
    if c==len(b):
        print("YES")
    else:
        print("NO")
