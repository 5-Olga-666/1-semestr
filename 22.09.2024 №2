def prostota (y):
    z = 1
    i = 2
    while i**2<y:
        if y%i==0:
            z = 0
            break
    return z
def razlogenie (x):
    i = 2
    a = []
    while i**2<=x:
        if prostota(i)==1:
            while x%i==0:
                a.append(i)
                x = x//i
        i=i+1
    if x>1:
        a.append (x)
    return a
N = int(input())
print (razlogenie(N))
