a,b=map(str,input().split())
c=list(map(str,input().split()))
for i in c:
      if i in b:
            print('yes')
            break
else:
      print('no')
