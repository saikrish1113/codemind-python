n=int(input())
m=list(map(int,input().split()))
c=0
for i in m:
    c=c*10+i
a=str(c)
print(int(a,2))