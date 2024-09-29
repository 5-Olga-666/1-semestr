from math import *
a,b = map(int, input().split())
def NOD(a,b):
    if a==0 or b==0:
        return a+b
    if a>b:
        return NOD(a%b, b)
    else:
        return NOD(a, b%a)
d = NOD(a,b)
x=max(a,b)*(-1)
y=(-1)*(a/b)*x+(d/b)
for i in range(max(a,b)*(-1), max(a,b)):
    u=(-1)*(a/b)*i+(d/b)
    if u==u//1 and abs(i)+abs(u)<abs(x)+abs(y):
            x=i
            y=u
print(x,y,d)

        
