n=int(input())
for i in range(0,100):
    s=i+1
    if n%s*i==0:
        if n==s*i:
            break
    i=i+1
k=n//i
if k==i+1:
    print("YES")
else:
    print("NO")