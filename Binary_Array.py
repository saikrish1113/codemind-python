n=int(input())
m=list(map(int,input().split()))
c=0
for i in m:
    if i==0 or i==1:
        c+=1
print(c==n)