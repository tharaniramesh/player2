n=int(input())
a=list(map(int,input().split()))
d=sorted(a,reverse=True)
for i in d:
    print(i,end="")
