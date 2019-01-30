a,b=map(int,input().split())
d=[]
for i in range(b,0,-1):
    if a%i==0 and b%i==0:
        d.append(i)
print(max(d))
