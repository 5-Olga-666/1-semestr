x = [int(s1) for s1 in input().split()]
y = [int(s2) for s2 in input().split()]
#<xy>
a=0
for i in range(len(x)):
    a=a+x[i]*y[i]
a=a/(len(x))
#<x>
c=0
for i in range(len(x)):
    c=c+x[i]
c=c/(len(x))
#<y>
d=0
for i in range(len(y)):
    d=d+y[i]
d=d/(len(x))
#<x^2>
e=0
for i in range(len(x)):
    e=e+x[i]**2
e=e/(len(x))
#<x>^2
f=c**2
k=(a-c*d)/(e-f)
b=d-k*c
print(k, b)
     
