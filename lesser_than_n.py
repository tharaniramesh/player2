n=int(input())
a=map(int,input().split())
c=0
for i in a:
      if(i<n):
            if c==0:
                  print(i,end="")
                  c+=1
            else:
                   print('',i)
