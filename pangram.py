s=input()
a={}
c=0
for j in range(97,123):
    a.update({chr(j):0})
b=s.replace(" ","")
f=b.lower()
for i in f:
    d=f.count(i)
    a.update({i:d})
for x,y in a.items():
    if y>=1:
        c+=1
if c==26:
    print('yes')
else:
    print('no')
