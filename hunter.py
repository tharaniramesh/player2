import collections
n=int(input())
l=list(map(str,input().split()))
a=[]
for i in l:
    s=l.count(i)
    a.append(s)
w=max(a)   
fre=collections.Counter(l)
c=0
if w>1:
    for x,y in fre.items():
    
        if y>1:
            if c==0:
                print(x,end="")
                c+=1
            else:
                print("",x,end="")
else:
    print('unique')
