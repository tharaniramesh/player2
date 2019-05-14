s=input()
k=s.split(" ")
b=[]
for i in k:
     b.append(i[::-1])
print(*b)
