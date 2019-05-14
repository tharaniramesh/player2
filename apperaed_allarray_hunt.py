n,k=map(int,input().split())
c=[]
for i in range(0,n):
      a=input().split()
      c.append(a)
m=c[0]
n=len(m)
for i in range(0,len(c)):
      j=0
      while(j<len(m)):
            if m[j] not in c[i]:
                  del (m[j])
                  j-=1
            j+=1
b=sorted(m)
print(*b)
