n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    if i%2==0 and a[i]%2==1:
       b.append(a[i])
    elif i%2!=0 and a[i]%2==0:
        b.append(a[i])
print(*b)  
