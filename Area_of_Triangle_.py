a,b,c=map(int,input().split())
x=(a+b+c)/2
s=(x*(x-a)*(x-b)*(x-c))**0.5
print('%.2f'%s)